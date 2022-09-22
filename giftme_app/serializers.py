from rest_framework import serializers

from .models import Giftme


class GiftmeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Giftme
        fields = '__all__'

