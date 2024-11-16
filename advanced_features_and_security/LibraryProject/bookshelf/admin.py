from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'date_of_birth', 'profile_photo', 'is_staff')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
# Register your models here.
