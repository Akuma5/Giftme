from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from giftme_app.views import ListView, UpdateView, DestroyView, GiftmeLikeView, AddToFriend, FriendsList, WishList
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Главная/', ListView.as_view()),
    path('Просмотр продукта/<int:pk>', UpdateView.as_view()),
    path('<int:product_pk>/like', GiftmeLikeView.as_view()),
    path('Удалить продукт/', DestroyView.as_view),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('drf-auth/', include('rest_framework.urls')),

    path('add_friend/<int:user_id>/', AddToFriend.as_view()),
    path('my_friends/', FriendsList.as_view()),

    path('wishlist/', WishList.as_view())
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

