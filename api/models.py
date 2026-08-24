from django.db import models 
from django.contrib.auth.models import User 

class Postz(models.Model): 
    CATEGORY_CHOICES = [ 
        ("News", "News"), 
        ("Sports", "Sports"), 
        ("Games", "Games"), 
        ("Movies/shows", "Movies/shows"), 
        ("Music", "Music"), 
        ("Other", "Other"), 
    ] 
    title = models.CharField(max_length=45) 
    text = models.TextField() 
    category = models.CharField( 
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default="News", 
    ) 
    author = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name="postz", 
    ) 
    created_at = models.DateTimeField(auto_now_add=True) 
    class Meta: 
        ordering = ["-created_at"] 
    def __str__(self): 
        return self.title 

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    postz = models.ForeignKey(
        Postz,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.text[:40]
