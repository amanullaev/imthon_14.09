from django import forms
from .models import CustomUser


class AccountForm(forms.ModelForm):
    first_name_uz = forms.CharField()
    first_name_ru = forms.CharField(required=False)
    first_name_en = forms.CharField(required=False)

    last_name_uz = forms.CharField()
    last_name_ru = forms.CharField(required=False)
    last_name_en = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        exclude = ['first_name', 'last_name']
