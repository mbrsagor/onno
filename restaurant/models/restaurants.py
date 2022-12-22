import random
import string

from accounts.models import User
from base.models.base import BaseEntity
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save


class Restaurant(BaseEntity):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='restaurant')
    name = models.CharField(max_length=120)
    sub_domain = models.CharField(max_length=180, blank=True, null=True)
    avatar = models.ImageField(upload_to='restaurantAvatar', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def owner_name(self):
        return self.owner.username

    def save(self, *args, **kwargs):
        self.sub_domain = slugify(
            self.name + '-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)))
        super(Restaurant, self).save(*args, **kwargs)


class RestaurantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_restaurant', null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_users')

    def __str__(self):
        return self.user.email
