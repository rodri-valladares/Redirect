from django.contrib import admin
from .models import Redirect
# Register your models here.

class RedirectAdmin(admin.ModelAdmin):
    list_display=['key','url','active','updated_at','created_at']

admin.site.register(Redirect, RedirectAdmin)