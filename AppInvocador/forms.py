from django import forms


class formSetInvocador(forms.Form):
    nombre = forms.CharField(max_length=30)
    nick = forms.CharField(max_length=30)
    email = forms.EmailField()
