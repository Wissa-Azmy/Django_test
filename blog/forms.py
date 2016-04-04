from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):  # To create a form from a Model
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        # exclude = ['fieldName'] :  used to include all except for this one

# ------- FORM VALIDATION --------
    def clean_email(self): # The method cleans whatever field comes after the _
        email = self.cleaned_data.get('email') # Save the cleaned data
        email_base, provider = email.split('@')  # The method splits the string into two parts and assigns them to the provided list of variables accordingly
        domain, extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError('Please Use a Gmail Account')
        if not extension == 'com':
            raise forms.ValidationError('Please Use a .com Extension')
        return email # To reverse the clean method above

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # wrtie Validation code
        return full_name


class ContactForm(forms.Form):  # To create a raw form with any DB implementation
    full_name = forms.CharField(required = False)
    email = forms.EmailField()
    message = forms.CharField()