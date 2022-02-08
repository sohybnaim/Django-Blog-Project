from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'age', 'email','phone_number','country')