from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65,widget=forms.TextInput(attrs={
        'placeholder':'Enter Username',
        'class':'w-full rounded-lg px-6 py-4 border border-solid border-gray-600'
    }) )
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
            'class':'w-full rounded-lg px-6 py-4 border border-solid border-gray-600'
        }
        
    ))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter username for your account',
        'class':'w-full px-6 py-4  rounded-lg border border-solid border-gray-600'
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your Email Address',
        'class':'w-full px-6 py-4  rounded-lg border border-solid border-gray-600'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'w-full px-6 py-4  rounded-lg border border-solid border-gray-600'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'w-full px-6 py-4  rounded-lg border border-solid border-gray-600'
    }))


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
    