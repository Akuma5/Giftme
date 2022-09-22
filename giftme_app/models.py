from django.contrib.auth.models import User
from django.db import models


class Giftme(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,)

    def __str__(self):
        return self.title


class MagazineLike(models.Model):
    """ Класс лайка """
    product = models.ForeignKey('giftme_app.Giftme', models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, models.SET_NULL, null=True)
