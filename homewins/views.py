# Create your views here.
from rest_framework import viewsets, permissions

from homewins.models import Profile
from homewins.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
