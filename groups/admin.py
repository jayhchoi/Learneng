from django.contrib import admin

from .models import Group, Comment

admin.site.register(Group)
admin.site.register(Comment)