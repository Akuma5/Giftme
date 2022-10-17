from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Giftme(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", db_index=True)
    content = models.TextField()
    image = models.ImageField(upload_to='magazine/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GiftmeLike(models.Model):
    """ Класс лайка """
    product = models.ForeignKey('giftme_app.Giftme', models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, models.SET_NULL, null=True)


class GiftmeImage(models.Model):
    """Фото объекта"""
    image = models.ImageField(verbose_name='Фото')
    image_link = models.ForeignKey(Giftme, verbose_name='Ссылка на объект', on_delete=models.CASCADE,
                                   related_name='photo')



