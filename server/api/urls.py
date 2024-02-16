from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('rota_users', RotaUserViewSet, basename='rota_users')
router.register('user', UserViewSet, basename='user')
router.register('cases', CaseViewSet, basename='cases')


API_URLS = [
    path("api/", include(router.urls)),
]

