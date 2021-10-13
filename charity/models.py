from django.db import models

# Create your models here.

class charity(models.Model):
  charity_id=models.IntegerField()
  charityname=models.CharField(max_length=30)
  charityaddress=models.CharField(max_length=30)
  phonenumber=models.IntegerField()

  def __str__(self):
      return self.charityname