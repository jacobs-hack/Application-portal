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

    email = models.EmailField(help_text="Your email address", unique=True)
    
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

    # TODO: Add a field for CV


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