from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
from homewins import views

router = DefaultRouter()
router.register(r'homewins/profile', views.ProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
