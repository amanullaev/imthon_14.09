from django.contrib import admin
from .models import UserModel


# @admin.site.register(UserModel)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name',)


admin.site.register(UserModel)
