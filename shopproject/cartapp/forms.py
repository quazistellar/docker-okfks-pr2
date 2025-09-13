from django import forms
from shop.models import Order



class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=30, initial=1, label='Количество',
                                 widget=forms.NumberInput(attrs={'class': 'form-control dark-input'}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'comment', 'first_name', 'last_name', 'middle_name']
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control dark-input', 'rows': 4}),
            'comment': forms.Textarea(attrs={'class': 'form-control dark-input', 'rows': 4}),
            'first_name': forms.TextInput(attrs={'class': 'form-control dark-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control dark-input'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control dark-input'}),
        }