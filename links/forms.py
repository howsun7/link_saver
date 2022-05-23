from django import forms
from .models import Link, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url', 'categories',)
