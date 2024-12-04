# forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prodOwner', 'phone_number', 'price', 'title', 'description', 'image']