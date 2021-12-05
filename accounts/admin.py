from django.contrib import admin

# Register your models here.

from accounts.models import Profile, TypeProfile
admin.site.register(Profile)
admin.site.register(TypeProfile)
