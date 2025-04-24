from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=15)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

