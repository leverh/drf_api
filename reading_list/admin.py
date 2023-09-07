from django.contrib import admin
from .models import Book, UserBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

# Register UserBook with the default admin interface


admin.site.register(UserBook)