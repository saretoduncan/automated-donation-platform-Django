import statistics

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BeneficiarySerializer

# Create your views here.

class BeneficiaryList(APIView):
    def get(self, request, id):
        Beneficiiaries = Beneficiary.objects.all()
        serializers = BeneficiarySerializer(projects, many=True)
        return Response(serializers.data)


def post(self, request):
    user = request.data
    serializer = self.serializer_class(data=user)
    # serializer.is_valid(raise_exception=True)
    serializer.save()
    user_data = serializer.data

    return Response(user_data) 
