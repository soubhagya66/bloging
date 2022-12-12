from django.contrib import admin
from atexit import register
from .models import Author,Tag,Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display=("title","date","author",)
    list_filter=("tags","date","author",)
    prepopulated_fields={"slug":("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","text")    

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)