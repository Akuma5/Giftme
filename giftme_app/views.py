
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Giftme, MagazineLike
from .serializers import GiftmeSerializers


class ListView(generics.ListCreateAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UpdateView(generics.RetrieveUpdateAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticated, )


class DestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Giftme.objects.all()
    serializer_class = GiftmeSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MagazineLikeView(APIView):
    """ Добавляет лайк """

    def get(self, request, product_pk):
        created = MagazineLike.objects.filter(product_id=product_pk, user=request.user).exists()
        if created:
            MagazineLike.objects.filter(
                product_id=product_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            MagazineLike.objects.create(product_id=product_pk, user=request.user)
            return Response({'success': 'liked'})

