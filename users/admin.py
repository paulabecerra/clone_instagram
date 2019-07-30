#User admin classes#
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Profile Admin#
    list_display = ('user', 'phone_number', 'website', 'picture')
    list_display_links = ('user', 'phone_number')
    list_editable = ('website', 'picture')

    search_fields = (
        'user__email',
        'user_username',
        'user__first__name',
        'user__last__name',
        'phone_number')

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (
            ('website', 'phone_number'),
            ('biography')
                ),
        }),
        ('Metadata', {
            'fields': (
                'created',
                'modified'),
        }),
    )
    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    #Profile in-line admin for users#
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    #add profile admin to base user admin#
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
