from django.contrib import admin
from .models import Post, Author, Tag, Comment

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)

# Register your models here.
