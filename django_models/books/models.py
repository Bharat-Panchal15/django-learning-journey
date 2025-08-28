from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.IntegerField(default=100)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"