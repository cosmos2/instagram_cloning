from rest_framework import serializers
from . import models
from nomadgram.images import serializers as images_serializers
from nomadgram.users import serializers as users_serializers


class NotificationSerializer(serializers.ModelSerializer):

    creator = users_serializers.ListUserSerializer()
    image = images_serializers.SmallImageSerializer()
    class Meta:
        model = models.Notification
        fields = '__all__'