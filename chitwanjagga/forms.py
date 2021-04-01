from django import forms

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserModelForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =('username', 'email', 'first_name', 'last_name', 'password')

        def clean(self):

            cleaned_data = super(UserModelForm, self).clean()
            password = cleaned_data['password']
            confirmpassword = cleaned_data['confirmpassword']
            if password != confirmpassword:
                raise forms.ValidationError('password not match')

