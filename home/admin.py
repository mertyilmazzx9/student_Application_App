from django.contrib import admin
from .models import Basvuru


class BasvuruAdmin(admin.ModelAdmin):
    list_display = ['name','surname']


admin.site.register(Basvuru,BasvuruAdmin)
