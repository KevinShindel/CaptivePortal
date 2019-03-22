from django.contrib import admin
from .models import Main

# Register your models here.
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('login','password')
