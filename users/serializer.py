from rest_framework import serializers
from .models import FirebaseUsers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseUsers
        fields = '__all__'


