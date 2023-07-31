import django_filters
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import AddedSerializer
from .models import Added


class AddedViewSet(viewsets.ModelViewSet):
    """Adding method post"""
    queryset = Added.objects.all()
    serializer_class = AddedSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user__email"]

    def create(self, request, *args, **kwargs):
        serializer = AddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Record added to database',
                'id': serializer.data['id'],
            })

        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': 400,
                'message': 'Bad request',
                'id': None,
            })

        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': 500,
                'message': 'Error connecting to database',
                'id': None,
            })

    def partial_update(self, request, *args, **kwargs):
        added = self.get_object()
        serializer = self.get_serializer(added, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': 1,
                'message': 'Post updated'
            })

        else:
            return Response({
                'state': 0,
                'message': serializer.errors
            })
