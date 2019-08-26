from django.contrib import admin
from .models import Post, Comment, Tag, Report

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Tag)

# Register your models here.
