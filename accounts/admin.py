from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
from .forms import UserCreateForm, UserChangeForm
# from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class MyAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    model = User
    add_form = UserCreateForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'phone', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('avatar', 'bio',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'gender', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, MyAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
