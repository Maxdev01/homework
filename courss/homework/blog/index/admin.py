from django.contrib import admin

# Register your models here.

from .models import Atik

@admin.register(Atik)
class AtikAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tit',)}