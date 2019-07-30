#User forms

#Django
from django import forms

#Models
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    #Signup Form#
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    confirmation_password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput)

    def clean_username(self):
        #Username must be unique#
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        #Verify password confirmation match#
        data = super().clean()

        password = data['password']
        password_confirmation = data['confirmation_password']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        return data

class ProfileForm(forms.Form):
    website = forms.URLField(label='Website', max_length=200, required=True)
    phone_number = forms.IntegerField(label='Phone Number', required=False)
    biography = forms.CharField(label='Biography', max_length=500, required=False)
    picture = forms.ImageField(label='Picture')

class SignUpForm1(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='First Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=200, required=True)
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', required=True)
    biography = forms.CharField(label='Bio', max_length=500, required=False)
    website = forms.URLField(label='Website', max_length=200, required=False)
    phone_number = forms.IntegerField(label='Phone Number', required=False)
