from django.contrib import admin
from .models import Category,Subcategory,Article,CustomUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','facebook','twitter','instagram',]

admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(Category)

admin.site.register(Subcategory)

class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['subcategory','title','active','created_by','total_views',]
    prepopulated_fields = {"slug": ("title",)}


    fieldsets = (
        ('Type of article', {
            'fields': ('subcategory',)
        }),
        ('Content', {
            
            'fields': ('title', 'image','story','created_by','tags','source'),
        }),
        ('Advance Options',{
            'classes': ('collapse',),
            'fields': ('active', 'slug'),
        })
    )



admin.site.register(Article,ArticleAdmin)


