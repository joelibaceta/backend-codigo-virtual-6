from store.models import Category, Product
from django.contrib import admin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'products_count')

    def products_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'local_price', 'category', 'brand', 'stock', 'sku')

    def local_price(self, obj):
        return f"S/. {obj.price}"

admin.site.register(Product, ProductAdmin)