from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'body',
        'preview',
        'created_at',
        'published',
        'views',
    )
