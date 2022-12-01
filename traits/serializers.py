from rest_framework import serializers, validators
from .models import Trait


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=20,
    )
    create_at = serializers.DateTimeField(read_only=True)
