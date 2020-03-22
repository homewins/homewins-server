from rest_framework import serializers

from homewins.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ['created', 'id', 'score', 'owner', 'ssid', 'latlong']
