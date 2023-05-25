from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(label='이름')
    login_phone_number = forms.CharField(label='전화번호', widget=forms.PasswordInput)
