from django.db import models

# Create your models here.
class User(models.Model):

    date = models.CharField(max_length=30)
    diary = models.CharField(max_length=30)

    
    def __str__(self):
        return self.date