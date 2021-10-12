from django.db.models import fields
from rest_framework import serializers
from . models import beneficiary
 
class beneficiarySerializers(serializers.ModelSerializer):

  class Meta:
    model = beneficiary

    fields= '__all__'
