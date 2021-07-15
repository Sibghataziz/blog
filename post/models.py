from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to='pics', blank=True)
    body = models.TextField(blank=False)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    #image = models.ImageField(upload_to='pic', blank=True)
    commented_date = models.DateTimeField(auto_now_add=True)
