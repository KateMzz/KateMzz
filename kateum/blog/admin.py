from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_posted', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ("title",)



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
