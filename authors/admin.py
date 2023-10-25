from django.contrib import admin
from .models import Author, Post, Comment
from django.utils.html import format_html
 
class AdminAuthor(admin.ModelAdmin):
    # к списку
    list_display = ["pk", "first_name", "last_name", "birthday", 'photo', 'image_preview']
    list_display_links = ["pk", "first_name", "last_name"]
    list_editable = ['birthday', 'photo']
    ordering = ["pk"]
    search_fields = ["email", "last_name"]
    # list_per_page = 2
    # к объекту
    fields = [('first_name', 'last_name'), 'email']
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["first_name", "last_name"],
    #         },
    #     ),
    #     (
    #         "Подробности",
    #         {
    #             "classes": ["collapse"],
    #             "description": "Birthday & Email",
    #             "fields": ["birthday", 'email'],
    #         },
    #     ),
    # ]
    
    def image_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="50">')
        return 'No image'


admin.site.register(Author, AdminAuthor)
admin.site.register(Post)
admin.site.register(Comment)
