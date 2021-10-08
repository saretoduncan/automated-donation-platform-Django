from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    cartegory = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=10,blank =True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

