from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 3)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={
            'class': 'form-select mt-1 mb-1 block w-1/4 border-gray-300 rounded-md shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

