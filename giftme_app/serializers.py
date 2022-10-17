from rest_framework import serializers

from .models import Giftme, GiftmeImage


class GiftmeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Giftme
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftmeImage
        fields = "__all__"
