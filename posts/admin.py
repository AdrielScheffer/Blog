from atexit import register
import site
from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)