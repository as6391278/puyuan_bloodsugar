from django.db import models

# Create your models here.

class User(models.Model):

    user_name = models.CharField(max_length=30)

    blood_high = models.CharField(max_length=30)
    
    blood_low = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user_name