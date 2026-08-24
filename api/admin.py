from django.contrib import admin 
from .models import Postz, Comment 

@admin.register(Postz) 
class PostzAdmin(admin.ModelAdmin): 
    list_display = ["title", "category", "author", "created_at"] 

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin): 
    list_display = ["text", "author", "postz", "created_at"]