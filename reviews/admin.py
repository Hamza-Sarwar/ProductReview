from django.contrib import admin
from .models import Product, Category, Company, ProductSize, ProductSite, Comment
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass
@admin.register(ProductSite)
class ProductSiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Product Review Admin"