from rest_framework.viewsets import ModelViewSet
from core.models import Entity
from core.serializers import EntitySerializer


class EntityViewSet(ModelViewSet):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()
