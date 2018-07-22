from django import forms
from django.contrib.auth import password_validation

from hacker.models import Hacker, HackathonApplication, AcademicData, Organizational, CV, DataRetentionAccept
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class RegistrationForm(forms.ModelForm):
    """ A form for registering users """

    _username_help_text = """
        Select your username for the JacobsHack Application Portal. 
        We recommend the first leter of your first name and full last name 
        e.g. <em>hackerman</em> for <em>Huber Ackerman</em>
    """

    username = forms.SlugField(label='Username',
                               help_text=_username_help_text)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        strip=False,
        widget=forms.PasswordInput,
        help_text='Re-enter your password'
    )

    # TODO: Update text for terms and conditions

    class Meta:
        model = Hacker
        fields = ['firstName', 'middleName', 'lastName', 'email', 'nationality']
        labels = {
            "firstName": "First Name",
            "middleName": "Middle Name",
            "lastName": "Last Name",
        }

    def clean(self):
        # individual field's clean methods have already been called
        cleaned_data = self.cleaned_data

        # check that the passwords are identical
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error('password2', forms.ValidationError(
                "Please make sure that the password you entered is correct. "))
            raise forms.ValidationError("Please correct the error below.")

        # check that the username doesn't already exist
        username = cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            self.add_error('username', forms.ValidationError(
                "This username is already taken, please pick another. "))
            raise forms.ValidationError("Please correct the error below.")


        return super(RegistrationForm, self).clean()


class HackerForm(forms.ModelForm):
    class Meta:
        model = Hacker
        fields = ['firstName', 'middleName', 'lastName', 'email', 'nationality']


class AcademicForm(forms.ModelForm):
    """ A form for saving the users academic data """

    class Meta:
        model = AcademicData
        fields = [
            'university', 'degree', 'year',
        ]
        labels = {
            'university': 'Which university are you from?',
            'degree': 'Degree',
            'year': 'Expected Graduation',
        }


class ApplicationForm(forms.ModelForm):
    """ A form for the Application of a Hacker """

    class Meta:
        model = HackathonApplication
        fields = [
            'whyJacobsHack', 'whatHaveYouBuilt', 'firstHackathon'
        ]
        labels = {
            'whyJacobsHack': 'Why do you want to come to JacobsHack?',
            'whatHaveYouBuilt': 'What projects have you worked on?<br />' +
                                'What have you built?',
            'firstHackathon': ''
        }


class OrganizationalForm(forms.ModelForm):
    """ A form for saving the users Organizational Data"""

    class Meta:
        model = Organizational
        fields = [
            'shirtSize', 'needVisa', 'needReimbursement', 'dietaryRequirements', 'comments'
        ]
        labels = {
            'shirtSize': 'T-Shirt Size',
            'needVisa': '',
            'needReimbursement': '',
            'dietaryRequirements': 'Dietary Requirements',
            'comments': 'Other Organizational Comments'
        }

class CVForm(forms.ModelForm):
    """ A form for saving CV Data"""
    class Meta:
        model = CV
        fields = [
            'cv'
        ]

class DataRetentionAcceptForm(forms.ModelForm):
    """ A form for privacy statements """
    class Meta:
        model = DataRetentionAccept
        fields = [
            'mlhContestTerms', 'mlhCodeOfConduct', 'GDPRClause'
        ]

        labels = {
            "mlhContestTerms" : mark_safe("StatementI agree to the terms of "
                                              "both the <a href='https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions'>"
                                              "MLH Contest Terms and Conditions</a> and the <a href='https://mlh.io/privacy'>"
                                              "MLH Privacy Policy </a>. Please note that you may receive pre and post-event "
                                              "informational e-mails and occasional messages about hackathons from MLH as "
                                              "per the MLH Privacy Policy."),

            "mlhCodeOfConduct" : mark_safe("I will at all times abide by and conform to the Major League Hacking "
                                               "<a href='https://mlh.io/code-of-conduct'>Code of Conduct </a> while at "
                                               "the event."),

            "GDPRClause" : mark_safe("I give consent to blah blah")
        }