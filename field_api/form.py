from django import forms
from .models import *


class StadiomForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_ru = forms.CharField(required=False)
    name_en = forms.CharField(required=False)

    location_uz = forms.CharField()
    location_ru = forms.CharField(required=False)
    location_en = forms.CharField(required=False)

    description_uz = forms.CharField()
    description_ru = forms.CharField(required=False)
    description_en = forms.CharField(required=False)

    class Meta:
        model = FieldModel
        exclude = ['name', 'location', 'description']