from modeltranslation.translator import translator, TranslationOptions
from account.models import CustomUser


class AccountTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


translator.register(CustomUser, AccountTranslationOptions)