from django.contrib import admin

from .models import Freedom

@admin.register(Freedom)
class FreedomAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'countryid', 'region', 'world_rank', 'inflation_pct')
    ordering = ['webname']
