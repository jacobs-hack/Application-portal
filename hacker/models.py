import collections
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from . import fields

class Hacker(models.Model):
    """ The information about a Hacker """

    profile = models.OneToOneField(User)

    # name and basic contact information
    firstName = models.CharField(max_length=255, help_text="Your first name")
    middleName = models.CharField(max_length=255, blank=True, null=True,
                                  help_text="Your middle name(s)")
    lastName = models.CharField(max_length=255, help_text="Your last name")

    @property
    def fullName(self):
        names = [self.firstName]

        if self.middleName is not None:
            names.append(self.middleName)

        names.append(self.lastName)
        return ' '.join(names)

    email = models.EmailField(help_text="Your private email address", unique=True)
    
    # TODO: Better handling of multiple nationalities
    nationality = fields.CountryField(
        help_text="You can select multiple options by holding the <em>Ctrl</em> key (or <em>Command</em> on Mac) while clicking",
        multiple=True)

    #
    # COMPONENTS MANAGEMENT
    #

    # The list of components know to this class
    components = collections.OrderedDict()

    @classmethod
    def register_component(cls, f):
        """ A decorator to add a component to the list of components """

        name = f.member.field.remote_field.name
        cls.components[name] = f
        return f

    def has_component(self, component):
        """ Checks if this alumni has a given component"""
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


@Hacker.register_component
class Address(models.Model):
    """ The address of an Hacker Member """

    member = models.OneToOneField(Hacker, related_name='address')

    address_line_1 = models.CharField(max_length=255,
                                      help_text="E.g. Campus Ring 1")
    address_line_2 = models.CharField(max_length=255, blank=True, null=True,
                                      help_text="E.g. Apt 007 (optional)")
    city = models.CharField(max_length=255, help_text="E.g. Bremen")
    zip = models.CharField(max_length=255, help_text="E.g. 28759")
    state = models.CharField(max_length=255, blank=True, null=True,
                             help_text="E.g. Bremen (optional)")
    country = fields.CountryField()

    addressVisible = models.BooleanField(default=False, blank=True,
                                         help_text="Include me on the alumni map (only your city will be visible to others)")


@Hacker.register_component
class SocialMedia(models.Model):
    """ The social media data of a Hacker """

    member = models.OneToOneField(Hacker, related_name='social')

    facebook = models.URLField(null=True, blank=True,
                               help_text="Your Facebook Profile (optional)")
    linkedin = models.URLField(null=True, blank=True,
                               help_text="Your LinkedIn Profile (optional)")
    twitter = models.URLField(null=True, blank=True,
                              help_text="Your Twitter Account (optional)")
    instagram = models.URLField(null=True, blank=True,
                                help_text="Your Instagram (optional)")
    homepage = models.URLField(null=True, blank=True,
                               help_text="Your Homepage or Blog")


@Hacker.register_component
class JacobsData(models.Model):
    """ The jacobs data of an Hacker """

    member = models.OneToOneField(Hacker, related_name='jacobs')

    college = fields.CollegeField(null=True, blank=True)
    graduation = fields.ClassField()
    degree = fields.DegreeField(null=True, blank=True)
    major = fields.MajorField()
    comments = models.TextField(null=True, blank=True,
                                help_text="e.g. exchange semester, several degrees etc.")


class Approval(models.Model):
    """ The approval status of a hacker """
    member = models.OneToOneField(Hacker, related_name='approval')

    approval = models.BooleanField(default=False, blank=True,
                                   help_text="Has the user been approved by an admin?")

    gsuite = models.EmailField(blank=True, null=True,
                               help_text="The G-Suite E-Mail of the user", unique=True)


@Hacker.register_component
class Skills(models.Model):
    """ The skills of a Hacker """

    member = models.OneToOneField(Hacker, related_name='skills')

    otherDegrees = models.TextField(null=True, blank=True)
    spokenLanguages = models.TextField(null=True, blank=True)
    programmingLanguages = models.TextField(null=True, blank=True)
    areasOfInterest = models.TextField(null=True, blank=True,
                                       help_text="E.g. Start-Ups, Surfing, Big Data, Human Rights, etc")
    alumniMentor = models.BooleanField(default=False, blank=True,
                                       help_text="I would like to sign up as an alumni mentor")
