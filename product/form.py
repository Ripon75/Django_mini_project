from django import forms
from django.forms import fields
from .models import insertProduct

class updateProduct(forms.ModelForm):
    class Meta:
        model=insertProduct
        fields=["name","slug","description"]
