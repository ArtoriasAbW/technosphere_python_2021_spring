from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser

#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'birthdate']
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('birthdate', 'email')}),)
#     fieldsets = UserAdmin.fieldsets


admin.site.register(CustomUser)
