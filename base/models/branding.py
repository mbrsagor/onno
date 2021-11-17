from django.db import models
from restaurant.models.outlets import Outlet

from base.models.base import BaseEntity


class Branding(BaseEntity):
    title = models.CharField(max_length=100, default='My site')
    outlet = models.OneToOneField(Outlet, on_delete=models.CASCADE, related_name='outlet_branding')
    message = models.TextField()
    cover_photo = models.ImageField(upload_to='application/% Y/% m/% d/', blank=True, null=True)
    favicon = models.ImageField(upload_to='application/% Y/% m/% d/', blank=True, null=True)

    def __str__(self):
        return self.title[:30]
