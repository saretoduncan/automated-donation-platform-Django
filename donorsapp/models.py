from django.db import models

# Create your models here.

class donors(models.Model):
  donor_id=models.IntegerField()
  donorname=models.CharField(max_length=30)
  emailaddress=models.CharField(max_length=30)
  phonenumber=models.IntegerField()

  def __str__(self):
      return self.donorname