from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from . models import donors
from . serializers import donorsSerializers

class donorsList(APIView):

  def get(self, request):
    donors1= donors.objects.all()
    serializers=donorsSerializers(donors1, many=True)
    return Response(serializers.data)

  def post(self):
    pass  
