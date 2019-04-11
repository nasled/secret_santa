from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(label='Enter Name', max_length=100)
    user_email = forms.CharField(label='Enter Email', max_length=100)