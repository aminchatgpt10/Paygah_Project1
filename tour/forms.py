from django import forms
from .models import tour


class tourform(forms.ModelForm):
    class Meta:
        model = tour
        fields = ['title', 'price', 'state', 'location', 'area', 'rooms', 'bathrooms']
