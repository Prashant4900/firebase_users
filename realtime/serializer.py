from rest_framework import serializers
from .models import DummyModel
from users.serializer import UserSerializer


class DummySerializer(serializers.ModelSerializer):
    user_json = UserSerializer(many=True, read_only=True)

    class Meta:
        model = DummyModel
        fields = ('id', 'uuid', 'name', 'user_json')
