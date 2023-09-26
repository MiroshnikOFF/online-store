from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('country', 'address', 'tin',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'is_current_version',)

