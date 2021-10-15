from django.db.models import fields
from rest_framework import serializers
from . models import beneficiary
 
class BeneficiarySerializers(serializers.ModelSerializer):

  class Meta:
    model = beneficiary

    fields= '__all__'
