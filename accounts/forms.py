from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65,widget=forms.TextInput(attrs={
        'placeholder':'Enter Username',
    }) )
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
        }
        
    ))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


    def clean_password(self):
        cd=self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('Password didn\'t match' )
        return cd['password2']
    
    def clean_email(self):
        data=self.cleaned_data['email']
        qs=User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use')
        return data
    