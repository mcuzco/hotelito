from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label=(''),
        max_length=12, 
        min_length=4, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(
        label=(''),
        max_length=12,
        min_length=4, 
        required=True,
        widget=(forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'})))
    email = forms.EmailField(
        label=(''),
        max_length=50,
        widget=(forms.TextInput(attrs={'placeholder': 'Ingrese su email'})))
    password1 = forms.CharField(
        label=_(''),
        widget=(forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'})),
        help_text=(''))
    password2 = forms.CharField(
        label=_(''), 
        widget=forms.PasswordInput(attrs={'placeholder': 'Comfirme su contraseña'}))
    username = forms.CharField(
        label=_(''),
        max_length=150,
        help_text=_(''),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese un usuario'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class SignipForm(AuthenticationForm):
    password = forms.CharField(
        label=_(''),
        widget=(forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'})))
    username = forms.CharField(
        label=_(''),
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese un usuario'}))
    class Meta:
        model = User
        fields = ('username', 'password')   