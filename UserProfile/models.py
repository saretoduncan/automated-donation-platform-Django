from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.

class Profile(models.Model):
    User = get_user_model()
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    user_bio=models.TextField(max_length=255)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True
    )
    def __str__(self):
        return self.user.username
