from rest_framework import serializers

from .models import Giftme, GiftmeImage, Friendship, Wish


class GiftmeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Giftme
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftmeImage
        fields = "__all__"


class FriendshipSerializer(serializers.ModelSerializer):
    get_friends_username = serializers.ReadOnlyField()

    class Meta:
        model = Friendship
        exclude = ['user_1', ]


class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wish
        fields = '__all__'
        read_only_fields = ['user',]