from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price')
  search_filds = ('name',)

admin.site.register(Product,ProductAdmin)
