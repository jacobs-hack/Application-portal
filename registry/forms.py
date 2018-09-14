from django import forms
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from hacker.models import Hacker, HackathonApplication, AcademicData, Organizational, CV, RSVP

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django_forms_uikit.widgets import DatePickerInput

import datetime

class HackerForm(forms.ModelForm):
    class Meta:
        model = Hacker
        fields = [
            'firstName', 'middleName', 'lastName', 
            'dob', 'gender', 'race',
            'email', 'phoneNumber',
            'nationality', 'countryOfResidence', 
            'jacobsHackTerms', 'mlhCodeOfConduct', 'mlhContestTerms',
        ]
        labels = {
            "firstName": "First Name",
            "middleName": "Middle Name",
            "lastName": "Last Name",
            
            "dob": "Date Of Birth",
            "race": "Race / Ethnicity",
            
            "phoneNumber": "Phone Number",
            "countryOfResidence": "Country Of Residence",
            
            "jacobsHackTerms": "JacobsHack! Terms & Conditions",
            "mlhCodeOfConduct": "MLH Code Of Conduct",
            "mlhContestTerms": "MLH Contest Terms & Privacy Policy",
        }
    
    dob = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, 
        label="Date Of Birth", 
        help_text="The date you were born. You need to be at least {} years of age to participate in jacobsHack!. Use either the datepicker widget or enter it in <em>%Y-%m-%d</em> format. ".format(settings.MIN_HACKER_AGE),
        widget=DatePickerInput()
    )
    
    def clean(self):
        # individual field's clean methods have already been called
        cleaned_data = self.cleaned_data

        # check that we have accepted the terms and conditions
        if not cleaned_data.get('jacobsHackTerms'):
            self.add_error('jacobsHackTerms', forms.ValidationError(
                "You need to accept the JacobsHack Terms and Conditions to apply to JacobsHack. "))
            raise forms.ValidationError("Please correct the error below. ")
        
        # check that we have accepted the MLH Code Of Conduct
        if not cleaned_data.get('mlhCodeOfConduct'):
            self.add_error('mlhCodeOfConduct', forms.ValidationError(
                "You need to accept the MLH Code of Conduct to apply to JacobsHack. "))
            raise forms.ValidationError("Please correct the error below. ")
        
        # check that we have accepted the MLT Terms & Conditions
        if not cleaned_data.get('mlhContestTerms'):
            self.add_error('mlhContestTerms', forms.ValidationError(
                "You need to accept the MLH Contest Terms & Conditions to apply to JacobsHack. "))
            raise forms.ValidationError("Please correct the error below. ")
        
        dob = cleaned_data.get('dob')
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < settings.MIN_HACKER_AGE:
            self.add_error('dob', forms.ValidationError(
                "We are not allowed to accept applications of minors for JacobsHack. Please apply once you are older than {} years of age. ".format(settings.MIN_HACKER_AGE)))
            raise forms.ValidationError("Please correct the error below. ")
        
        return super(HackerForm, self).clean()


class RegistrationForm(HackerForm):
    """ A form for registering users """

    _username_help_text = """
        Select your username for the JacobsHack! Application Portal. 
        We recommend the first letter of your first name and full last name 
        e.g. <em>hackerman</em> for <em>Huber Ackerman</em>. 
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
        help_text='Re-enter your password. '
    )

    def clean(self):
        # individual field's clean methods have already been called
        cleaned_data = self.cleaned_data

        # check that the passwords are identical
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            self.add_error('password2', forms.ValidationError(
                "Please make sure that the password you entered is correct. "))
            raise forms.ValidationError("Please correct the error below. ")

        # check that the username doesn't already exist
        username = cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            self.add_error('username', forms.ValidationError(
                "This username is already taken, please pick another. "))
            raise forms.ValidationError("Please correct the error below. ")
        
        return super().clean()

class AcademicForm(forms.ModelForm):
    """ A form for saving the users academic data """

    class Meta:
        model = AcademicData
        fields = [
            'school', 'degree', 'major', 'year',
        ]
        labels = {
            'year': 'Expected Graduation',
        }

class RSVPForm(forms.ModelForm):
    """ A form for saving the users RSVP data """
    going = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )
    class Meta:
        model = RSVP
        fields = [
            'going',
        ]
        labels = {
            'going': 'RSVP'
        }
        help_texts = {
            'going': 'Yes, I will come to jacobsHack! 2018'
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
            'needVisa': 'Visa',
            'needReimbursement': 'Travel Reimbursement',
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
