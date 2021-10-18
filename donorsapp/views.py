from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, views, generics
from . models import donors
from . serializers import donorsSerializers

class donorsList(APIView):

  serializer_class = donorsSerializers
  def get(self, request, id,):
    donors= Donors.objects.filter(id=id)
    serializers=donorsSerializers(donors, many=True)
    return Response(serializers.data)

  def post(self, request):
    user = request.data
    serializer = self.serializer_class(data=user)
    # serializer.is_valid(raise_exception=True)
    serializer.save()
    user_data = serializer.data

    return Response(user_data)
