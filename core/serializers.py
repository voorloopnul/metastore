from rest_framework.serializers import ModelSerializer
from core.models import Entity


class EntitySerializer(ModelSerializer):
    class Meta:
        model = Entity
        fields = "__all__"
