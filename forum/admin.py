from django.contrib import admin

# Register your models here.

from forum.models import Comment, Thread
admin.site.register(Comment)
admin.site.register(Thread)