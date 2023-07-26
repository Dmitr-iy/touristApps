from rest_framework import viewsets
from .serializers import AddedSerializer
from .models import Added


class AddedViewSet(viewsets.ModelViewSet):
    """Adding method post"""
    queryset = Added.objects.all()
    serializer_class = AddedSerializer
