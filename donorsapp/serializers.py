from django.db.models import fields
from rest_framework import serializers
from . models import donors
 
class donorsSerializers(serializers.ModelSerializer):

  class Meta:
    model = donors

    fields= '__all__'