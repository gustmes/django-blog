from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import uuid

class Author(models.Model):
    """Model for a post authors, linked to Users. """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, default="", help_text="Bio information for this author.")
    joined_date = models.DateField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.pk)])

class Tag(models.Model):
    """Model for post's tags."""
    name = models.CharField(max_length=100, unique=True, help_text="Enter the tag name.")

    def __str__(self):
        return self.name

class Post(models.Model):
    """Model for a blog post."""
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=200, help_text="Enter the post title.")

    content = models.TextField(max_length=1000, help_text="The main post content.")

    posted = models.DateTimeField()

    last_modified = models.DateTimeField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True, help_text="Add tags for the post.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    """Model for a post's comments."""
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    content = models.TextField(max_length=1000, help_text="Comment's text content.")

    posted = models.DateTimeField()

    last_modified = models.DateTimeField(null=True, blank=True)
