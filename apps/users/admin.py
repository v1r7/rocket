from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',  'email', 'phone_number', 'date_joined', 'action_wins',
    )

