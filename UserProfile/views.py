from django.shortcuts import render, redirect
from django.contrib import messages
from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import generics, status, views, permissions
# Create your views here.

class ProfileAPIView(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get (self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
