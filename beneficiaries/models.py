from django.db import models

# Create your models here.

class beneficiary(models.Model):
  beneficiary_id=models.IntegerField()
  beneficiaryname=models.CharField(max_length=30)
  beneficiaryaddress=models.CharField(max_length=30)
  phonenumber=models.IntegerField()

  def __str__(self):
      return self.beneficiaryname