from django.db.models import fields
from rest_framework import serializers
from . models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username','phone_number', 'user_bio','image')
    def validate(self, attrs):
        username = attrs.get('username', '')
        phone_number= attrs.get('phone_number', '')
        
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.update_profile(**validated_data)
   