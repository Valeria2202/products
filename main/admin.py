from django.contrib import admin

# Register your models here.
from .models import Product, Review, Client

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']

class ReviewInline(admin.TabularInline):
    model = Review
    fields = ['text', 'mark']



admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Client)