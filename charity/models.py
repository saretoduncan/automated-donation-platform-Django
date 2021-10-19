from django.db import models

# Create your models here.


class charity(models.Model):
    charity_id = models.IntegerField()
    charity_name = models.CharField(max_length=30)
    charity_address = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    charity_bio = models.TextField(max_length=255)
    trustdeed = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.charity_name
