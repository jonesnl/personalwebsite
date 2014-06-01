from django.db import models


class Author(models.Model):
    """Represents an author that can post on the blog"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Post(models.Model):
    """Represents a single post on the blog"""
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
