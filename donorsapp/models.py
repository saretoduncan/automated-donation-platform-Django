from django.db import models

# Create your models here.

class donors(models.Model):
  donor_name=models.CharField(max_length=30, default='no name')
  email_address=models.CharField(max_length=30, default=0)
  phone_number=models.IntegerField(default=0)
  image=models.ImageField(default='default.jpeg')
  donor_bio=models.TextField(max_length=255)

  def __str__(self):
      return self.donor_name