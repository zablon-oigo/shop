from django import forms 

PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
                                    widget=forms.Select(attrs={'class': 'border rounded px-4 py-2'}))
    override=forms.BooleanField(required=False,initial=False, widget=forms.HiddenInput)
    