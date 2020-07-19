from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filte = ('phone',)


admin.site.register(UserProfile, UserProfileAdmin)
