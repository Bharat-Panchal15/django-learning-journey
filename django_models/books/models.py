from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.IntegerField(default=100)
    is_published = models.BooleanField(default=True)
    genres = models.ManyToManyField(Genre,blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_long(self):
        return self.pages > 200
    
    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Books Records'