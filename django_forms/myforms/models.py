from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='post_images/',blank=True,null=True)