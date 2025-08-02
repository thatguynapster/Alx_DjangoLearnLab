from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to show in list view
    list_filter = ('author', 'publication_year')            # Filter sidebar
    search_fields = ('title', 'author')          
    
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ["username", "email", "first_name", "last_name", "is_staff", "date_of_birth"]
    search_fields = ["username", "email", "first_name", "last_name"]

admin.site.register(CustomUser, CustomUserAdmin)