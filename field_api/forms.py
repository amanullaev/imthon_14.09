from django import forms
from .models import FieldModel, BookingModel


class FieldForms(forms.ModelForm):
    name_uz = forms.CharField()
    name_en = forms.CharField(required=False)
    name_ru = forms.CharField(required=False)

    owner_uz = forms.CharField()
    owner_en = forms.CharField(required=False)
    owner_ru = forms.CharField(required=False)

    location_uz = forms.CharField()
    location_en = forms.CharField(required=False)
    location_ru = forms.CharField(required=False)

    description_uz = forms.CharField()
    description_en = forms.CharField(required=False)
    description_ru = forms.CharField(required=False)

    class Meta:
        model = FieldModel
        exclude = ['name', 'owner','location','description']


class BookingForms(forms.ModelForm):
    field_uz = forms.CharField()
    field_en = forms.CharField(required=False)
    field_ru = forms.CharField(required=False)

    user_uz = forms.CharField()
    user_en = forms.CharField(required=False)
    user_ru = forms.CharField(required=False)


    class Meta:
        model = FieldModel
        exclude = ['field', 'user']