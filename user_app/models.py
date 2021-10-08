from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.intagerField(primary_key=True)
    username = models.CharField(max_length=100)
    phone_number = models.intagerField(max_length=10,blank =False)
    email = models.EmailField()
    password = models.CharField(max_length=100)

