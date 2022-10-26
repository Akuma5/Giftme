from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Giftme, GiftmeLike, Friendship
from .serializers import GiftmeSerializers, FriendshipSerializer


class MagazineAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class ListView(generics.ListCreateAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = MagazineAPIListPagination


class UpdateView(generics.RetrieveUpdateAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticated,)


class DestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GiftmeLikeView(APIView):
    """ Добавляет лайк """

    def get(self, request, product_pk):
        created = GiftmeLike.objects.filter(product_id=product_pk, user=request.user).exists()
        if created:
            GiftmeLike.objects.filter(
                product_id=product_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            GiftmeLike.objects.create(product_id=product_pk, user=request.user)
            return Response({'success': 'liked'})


class AddToFriend(APIView):
    authentication_classes = [BasicAuthentication, ]
    def post(self, request, user_id, *args, **kwargs):
        current_user = request.user
        print(request.user)
        another_user = get_object_or_404(User, id=user_id)
        friendship = Friendship(user_1=current_user, user_2=another_user)
        friendship.save()
        return Response(status=status.HTTP_201_CREATED)


class FriendsList(generics.ListAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user_1=self.request.user)
        return queryset

