from django.contrib import admin

from .models import Flat, Complaint
from .models import Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner',)
    classes = ('collapse',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked',)
    fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('created_at', 'price', 'is_active', 'new_building', 'liked')}),
        ('Расположение', {'classes': ('collapse',), 'fields': ('town', 'town_district', 'address',)}),
        ('Описание объекта', {'classes': ('collapse',), 'fields': ('floor', 'rooms_number', 'living_area', 'has_balcony', 'construction_year', 'description',)}),
    )
    inlines = (OwnerInLine,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('author', 'flat',)
    raw_id_fields = ('author', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'phonenumber','pure_phonenumber'
        )
    raw_id_fields = (
        'flat',
        )
