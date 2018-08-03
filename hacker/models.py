import collections
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from . import fields
from .validators import validate_extension

from phonenumber_field.modelfields import PhoneNumberField

class Hacker(models.Model):
    """ The information about a Hacker """

    profile = models.OneToOneField(User)

    # name and basic contact information
    firstName = models.CharField(max_length=255, help_text="Your first name")
    middleName = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Your middle name(s)")
    lastName = models.CharField(max_length=255, help_text="Your last name")
    
    _gender_choices_ = ['Male', 'Female', 'Prefer Not to Answer']
    _gender_help_string_ = 'Pick one of {} or specify a custom one. '.format(' , '.join(map(repr, _gender_choices_)))
    gender = fields.FuzzyChoiceField(data=_gender_choices_, max_length=255, help_text=_gender_help_string_)
    
    _race_choices = ['American Indian or Alaskan Native', 'Asian / Pacific Islander', 'Black or African American', 'Hispanic', 'White / Caucasian', 'Prefer Not to Answer']
    _race_help_string = 'Pick one of {} or specify a custom one. '.format(' , '.join(map(repr, _race_choices)))
    race = fields.FuzzyChoiceField(data=_race_choices, max_length=255, help_text=_race_help_string)

    @property
    def fullName(self):
        names = [self.firstName]

        if self.middleName is not None:
            names.append(self.middleName)

        names.append(self.lastName)
        return ' '.join(names)

    email = models.EmailField(help_text="Your email address", unique=True)

    phoneNumber = fields.PhoneField()
    
    # TODO: Better handling of multiple nationalities
    nationality = fields.CountryField(
        help_text="You can select multiple options by holding the <em>Ctrl</em> key (or <em>Command</em> on Mac) while clicking",
        multiple=True)

    countryOfResidence = fields.CountryField()

    _terms_help_text = "I have read and agree to the <a href='/terms/' target='_blank'>JacobsHack Terms and Conditions</a>, including the <a href='/privacy/' target='_blank'>Privacy Policy</a>. "
    jacobsHackTerms = models.BooleanField(help_text=_terms_help_text, blank=False)

    _mlh_coc_help_text = "I have read and agree to the <a href='https://mlh.io/code-of-conduct'>MLH Code of Conduct</a>. "
    mlhCodeOfConduct = models.BooleanField(help_text=_mlh_coc_help_text, blank=False)

    _mlh_contest_terms = "I agree to the terms of both the <a href='https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions'>MLH Contest Terms</a> and the <a href='https://mlh.io/privacy' target='_blank'>MLH Privacy Policy</a>. "
    mlhContestTerms = models.BooleanField(help_text=_mlh_contest_terms, blank=False)

    _mlh_sharing_terms = "I authorize you to share my application/registration information for event administration, ranking, MLH administration, pre- and post-event informational e-mails, and occasional messages about hackathons in-line with the <a href='https://mlh.io/privacy' target='_blank'>MLH Privacy Policy</a>. "
    mlhSharingConsent = models.BooleanField(help_text=_mlh_sharing_terms, blank=True)

    #
    # COMPONENTS MANAGEMENT
    #

    # The list of components know to this class
    components = collections.OrderedDict()

    @classmethod
    def register_component(cls, f):
        """ A decorator to add a component to the list of components """

        name = f.hacker.field.remote_field.name
        cls.components[name] = f
        return f

    def has_component(self, component):
        """ Checks if this hacker has a given component"""
        try:
            _ = getattr(self, component)
            return True
        except ObjectDoesNotExist:
            return False

    def get_first_unset_component(self):
        """ Gets the first unset component or returns None if it
        already exists. """

        for c in self.__class__.components.keys():
            if not self.has_component(c):
                return c

        return None

    def __str__(self):
        return "Hacker [{}]".format(self.fullName)


class Approval(models.Model):
    """ The approval status of a hacker """
    hacker = models.OneToOneField(Hacker, related_name='approval')

    approval = models.BooleanField(default=False, blank=True,
                                   help_text="Has the application been approved?")


@Hacker.register_component
class AcademicData(models.Model):
    """ The academic data of a Hacker """

    hacker = models.OneToOneField(Hacker, related_name='academic')

    degree = fields.DegreeField(help_text="Which academic degree are you hoping to achieve?")
    year = fields.YearField(help_text="estimate the year during which you are expected to graduate")
    university = fields.UniField(help_text="use other if not listed")


@Hacker.register_component
class HackathonApplication(models.Model):
    """ The hackathon application  """

    hacker = models.OneToOneField(Hacker, related_name='application')

    whyJacobsHack = models.TextField()

    firstHackathon = models.BooleanField(default=False, blank=True,
                                   help_text="JacobsHack is my first Hackathon")

    whatHaveYouBuilt = models.TextField(help_text="E.g. GitHub Link, Devpost, Personal Projects ...")

@Hacker.register_component
class Organizational(models.Model):
    """ The organizational information about a Hacker """

    hacker = models.OneToOneField(Hacker, related_name='organizational')

    shirtSize = fields.ShirtSizeField(help_text="Select your EU T-Shirt size. ")

    needVisa = models.BooleanField(default=False, blank=True,
                                   help_text="I need a Visa to come to Germany and attend JacobsHack")

    needReimbursement = models.BooleanField(default=False, blank=True, 
                                    help_text="Are you coming from outside of Bremen?")

    dietaryRequirements = models.TextField(blank=True,
                                           help_text="e.g. Vegan, Vegetarian, Gluten-free ...")

    comments = models.TextField(blank=True,
                                help_text="If you are applying as a Team, mention the names of your teammates here. ")

import os.path
def upload_to(instance, filename):
    return 'cvs/{0}{1}'.format(instance.hacker.profile.username, os.path.splitext(filename)[1])

@Hacker.register_component
class CV(models.Model):
    """ The CV of a Hacker """

    hacker = models.OneToOneField(Hacker, related_name='cv')
    cv = models.FileField(
        upload_to=upload_to,
        validators=[validate_extension],
        null=True,
        blank=True,
        help_text="Your CV (optional)"
    )

    @property
    def has_cv(self):
        return self.cv and hasattr(self.cv, 'url')
    
    @property
    def internal_url(self):
        if self.has_cv:
            return settings.INTERNAL_PREFIX + self.cv.url
    
    @property
    def filename(self):
        return '{}.pdf'.format(self.hacker.profile.username)
