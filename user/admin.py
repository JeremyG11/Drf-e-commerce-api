from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'name',)
    list_filter = ('email', 'name', 'is_active', 'is_staff')
    ordering = ('-created_at',)

    list_display = ('email', 'name','is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('image','birthdate', 'address','biography',)}),
        ('Contact', {'fields':('phone', )})
    )

    formfield_overrides = {
        CustomUser.biography: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
