from django.contrib import admin
from blog.models import Author, Post

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
