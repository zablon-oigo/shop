from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','email','address','postal_code','city']
        widgets={
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter your first name',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter your last name',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
            'email':forms.TextInput(attrs={
                'placeholder':'Enter your email address',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
            'address':forms.TextInput(attrs={
                'placeholder':'Enter your addres loaction',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
            'postal_code':forms.TextInput(attrs={
                'placeholder':'Enter your postal code',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
            'city':forms.TextInput(attrs={
                'placeholder':'Enter your city',
                'class':'px-6 py-4 rounded-lg border border-gray-700 w-full '

            }),
        }