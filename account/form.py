from django import forms
<<<<<<< HEAD
class FieldForm(forms.Form):
    name = forms.CharField(max_length=100)
=======
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
>>>>>>> bee717d6443d4672c2ce8692a31160b8e8782c24
