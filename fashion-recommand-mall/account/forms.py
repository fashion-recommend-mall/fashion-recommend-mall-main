from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    '''
    Title : LoginForm
    This form is used in login templates
    Attributes:
        username (string) : this is marked with class form-control
        password (string) : this is marked with class form-control
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    '''
    Title : SignUpForm
    This form is used in register templates
    Attributes:
        username (string) : this is marked with class form-control
        email (string) : this is marked with class form-control
        password1 (string) : this is marked with class form-control
        password2 (string) : this is marked with class form-control
        meta (admin_user)
            fields = ('username', 'email', 'password1', 'password2')
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        """
        This is meta class for matching form data with admin user model!
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UploadImageForm(forms.Form):
    img1 = forms.ImageField()
    img2 = forms.ImageField()
    img3 = forms.ImageField()
    img4 = forms.ImageField()
    img5 = forms.ImageField()
    img6 = forms.ImageField()
    img7 = forms.ImageField()
    img8 = forms.ImageField()
    img9 = forms.ImageField()
    img10 = forms.ImageField()