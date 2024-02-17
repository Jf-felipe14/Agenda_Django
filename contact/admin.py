from django.contrib import admin
from .models import Contact,Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','email']
    ordering = ['id']
    # list_filter = ['created_date']
    search_fields = ['id','first_name','last_name']
    list_per_page = 10
    # list_editable= ['last_name']
    list_display_links = ['first_name']

@admin.register(Category)
class CategoryAAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-id']