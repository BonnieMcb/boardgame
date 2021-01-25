from django.contrib import admin
from .models import Product, Category, Mechanic

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'names',
        'price',
    )

    ordering = ('rank',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class MechanicAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Mechanic, MechanicAdmin)
