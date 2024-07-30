from django.db import models

# Create your models here.

class Article(models.Model):
    subject=models.CharField(max_length=25)
    title=models.CharField(max_length=50)
    date=models.DateField()
    article=models.TextField()

    def __str__(self):
        return self.title
    
