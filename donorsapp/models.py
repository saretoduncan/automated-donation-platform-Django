from django.db import models

# Create your models here.

class donors(models.Model):
  donor_name=models.CharField(max_length=30)
  email_address=models.CharField(max_length=30)
  phone_number=models.IntegerField()
  image=models.ImageField(default='default.jpeg')
  donor_bio=models.TextField(max_length=255)

  def __str__(self):
      return self.donorname
