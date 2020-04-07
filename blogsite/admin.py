from django.contrib import admin
from .models import Category,Subcategory,Article,Person
# Register your models here.

admin.site.register(Category)

admin.site.register(Subcategory)
admin.site.register(Person)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['subcategory','title','active','created_by',]
    prepopulated_fields = {"slug": ("title",)}


    fieldsets = (
        ('Type of article', {
            'fields': ('subcategory',)
        }),
        ('Content', {
            
            'fields': ('title', 'image','story','created_by','tags',),
        }),
        ('Advance Options',{
            'classes': ('collapse',),
            'fields': ('active', 'slug'),
        })
    )
admin.site.register(Article,ArticleAdmin)


