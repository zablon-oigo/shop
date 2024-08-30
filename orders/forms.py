from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
         'first_name': forms.TextInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         'last_name': forms.TextInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         'email': forms.EmailInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         'address': forms.TextInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         'postal_code': forms.TextInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         'city': forms.TextInput(attrs={
            'class': 'form-input mt-1 px-4 py-2 block w-full border-gray-300 border-2 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
         }),
         }

