from django.db.models import fields
from rest_framework import serializers
from . models import charity
 
class charitySerializers(serializers.ModelSerializer):

  class Meta:
    model = charity

    fields= '__all__'
