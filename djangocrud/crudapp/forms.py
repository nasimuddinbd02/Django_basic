from django import forms
from .models import Brand, Category,Product

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'