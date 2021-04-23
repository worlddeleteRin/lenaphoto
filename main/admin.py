from django.contrib import admin
from main.models import * 

# Register your models here.

class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    fields = [
        ('imgsrc')
    ]
class CategoryImageAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline]


admin.site.register(Category, CategoryImageAdmin)
# admin.site.register(CategoryImage, CategoryImageAdmin)
