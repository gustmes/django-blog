from django.contrib import admin

# Register your models here.
from . models import Author, Post, Comment, Tag

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)
