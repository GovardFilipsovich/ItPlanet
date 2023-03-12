from rest_framework import serializers
from RestApi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'password']
    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        ret.pop('password')
        return ret
