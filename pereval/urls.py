from django.urls import path, include
from rest_framework import routers
from pereval.views import AddedViewSet


router = routers.DefaultRouter()
router.register(r'submitdata', AddedViewSet, basename='submitdata')

urlpatterns = [
    path('', include(router.urls)),
]
