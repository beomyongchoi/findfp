from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Subscription(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    subscription_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
