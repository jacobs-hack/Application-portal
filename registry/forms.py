from django import forms
from django.contrib.auth import password_validation

from hacker.models import Hacker, Address, JacobsData, SocialMedia, \
    JobInformation, Skills
from django.contrib.auth.models import User
from django_forms_uikit.widgets import DatePickerInput


class RegistrationForm(forms.ModelForm):
    """ A form for registering users """
    username = forms.SlugField(label='Username',
                               help_text='Select your username for the JacobsHack Application Portal. '
                                         'We recommend the first leter of your first name and full last name e.g. <em>ppan</em> for <em>Peter Pan</em>')
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

    # TODO: Update text to point to:
    ## * MLH Contest Terms and Conditions ()
    ## * MLH Privacy Policy (https://mlh.io/privacy). Please note that you may receive pre and post-event informational e-mails and occasional messages about hackathons from MLH as per the MLH Privacy Policy.
    ## * Major League Hacking Code of Conduct https://mlh.io/code-of-conduct while at the event. 
    ## * Custom Privacy Policy
    ## TODO: place a trick phrase into the JacobsHack terms and conditions stating something like
    # "to claim any jacobshack prize, we might ask you a couple questions to confirm that you have read and agree to this policy. ""
    _tos_help_text = """
        I confirm that I have read, understood, and agree to: <br />

        <ul>
            <li>
                JacobsHack Terms and Conditions
            </li>
            <li>
                MLH Contest Terms and Conditions
            </li>
            <li>
                MLH Privacy Policy
            </li>
            <>
            <li>
                Major League Hacking Code of Conduct
            </li>
        </ul>
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
        cleaned_data = self.cleaned_data  # individual field's clean methods have already been called

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


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Hacker
        fields = ['firstName', 'middleName', 'lastName', 'email', 'nationality']

class AddressForm(forms.ModelForm):
    """ A form for the Address of an Alumni """

    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'zip', 'city',
                  'addressVisible', 'state',
                  'country']
        labels = {
            'addressVisible': ''
        }


class JacobsForm(forms.ModelForm):
    """ A form for saving the users Jacobs Data """

    class Meta:
        model = JacobsData
        fields = ['college', 'degree', 'graduation', 'major', 'comments']
        labels = {
            'college': 'College',
            'degree': 'Degree',
            'graduation': 'Class (first graduation)',
            'major': 'Major',
            'comments': 'Comments'
        }


# TODO: Check that social media links are actually valid links for the platform
class SocialMediaForm(forms.ModelForm):
    """ A form for saving the users Social Media Data """

    class Meta:
        model = SocialMedia
        fields = ['facebook', 'linkedin', 'twitter', 'instagram', 'homepage']


class SkillsForm(forms.ModelForm):
    """ A form for saving the users Skills Data """

    class Meta:
        model = Skills
        fields = [
            'otherDegrees', 'spokenLanguages', 'programmingLanguages',
            'areasOfInterest', 'alumniMentor'
        ]
        labels = {
            'otherDegrees': 'Degrees from other instiutions:',
            'spokenLanguages': 'Spoken Languages:',
            'programmingLanguages': 'Programming Languages',
            'areasOfInterest': 'Areas of interest/expertise',
            'alumniMentor': ''
        }


class JobInformationForm(forms.ModelForm):
    """ A form for saving the users Job Information Data """

    class Meta:
        model = JobInformation
        fields = ['employer', 'position', 'industry', 'job']