from django.contrib import admin
from .models import Post

# This allows blog posts to be accessible fromthe admin area
admin.site.register(Post)
