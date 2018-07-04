from django import forms
from django.contrib.auth import password_validation

from hacker.models import Hacker, HackathonApplication, AcademicData, Organizational, CV
from django.contrib.auth.models import User


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
    _tos_help_text = """
        I confirm that I have read, understood, and agree to each of the following:
        
        <p>
            <ul>
                <li>
                    <a href="/terms/" target="_blank">
                        JacobsHack Terms, Conditions &amp; Privacy Policy
                    </a>
                </li>
                <li>
                    <a href="https://github.com/MLH/mlh-policies/blob/master/prize-terms-and-conditions/contest-terms.md" target="_blank">
                        MLH Contest Terms and Conditions
                    </a>
                </li>
                <li>
                    <a href="https://mlh.io/privacy" target="_blank">
                        MLH Privacy Policy
                    </a>
                </li>
                <li>
                    <a href="https://mlh.io/code-of-conduct" target="_blank">
                        Major League Hacking Code of Conduct
                    </a>
                </li>
            </ul>
            
            In particular, I understand that I may be contacted via email by
            JacobsHack, MLH, or any of the sponsors as detailed in the 
            documents above. 
        </p>
    """

    tos = forms.BooleanField(label='Terms and Conditions',
                             help_text=_tos_help_text)

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

        # check that we have accepted the terms and conditions
        if not self.cleaned_data['tos']:
            self.add_error('tos', forms.ValidationError(
                "You need to accept the terms and conditions to continue. "))
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
            'whyJacobsHack', 'whatHaveYouBuilt', 'firstHackathon',
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