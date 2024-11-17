from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
     model = CustomUser
     list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
     list_filter = ['is_staff', 'is_superuser', 'date_of_birth']
     search_fields = ['username', 'email']
     ordering = ['username']

     fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
     )
     add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
     )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
# Register your models here.
