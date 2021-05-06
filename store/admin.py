from django.contrib import admin

# Register your models here.
from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' ,'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug' :('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','author','price','in_stock']
    #The attribute prepopulated_fields tells the admin application to automatically fill the field slug - in this case with the text entered into the title field.
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['in_stock']

    class Proxy:
        verbose_name = "In Stock"

