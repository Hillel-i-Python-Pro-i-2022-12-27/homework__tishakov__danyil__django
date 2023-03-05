from django.contrib import admin

from . import models


# admin.site.register(models.Contact)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality", "number", "is_auto_generated", "created_at", "modified_at")
    list_filter = ("is_auto_generated", "nationality")


class NatInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ("name", "modified_at")
    inlines = (NatInline,)
