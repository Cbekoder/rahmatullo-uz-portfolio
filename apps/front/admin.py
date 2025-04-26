from django.contrib import admin
from .models import Entrepreneur, Business, CoreValue, PortfolioItem, ContactMessage

@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
