from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class formSetInvocador(forms.Form):
    nombre = forms.CharField(max_length=30)
    nick = forms.CharField(max_length=30)
    email = forms.EmailField()


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Last Name"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Contraseña vieja"}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Nueva Contraseña"}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirmation de la nueva contraseña"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    avatar = forms.ImageField()
