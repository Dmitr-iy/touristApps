from rest_framework import viewsets
from .serializers import AddedSerializer
from .models import Added


class AddedViewSet(viewsets.ModelViewSet):
    """Addition of the POST method"""
    queryset = Added.objects.all()
    serializer_class = AddedSerializer
