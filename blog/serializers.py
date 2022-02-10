from rest_framework import serializers
from .models import Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','first_name', 'last_name', 'age', 'email','phone_number','country')

