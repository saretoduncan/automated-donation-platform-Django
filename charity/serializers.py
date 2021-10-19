from django.db.models import fields
from rest_framework import serializers
from . models import charity
 
class charitySerializers(serializers.ModelSerializer):

  class Meta:
    model = charity

    fields= [' charity_id','charityname','charity_address','phone_number','charity_bio','trustdeed']