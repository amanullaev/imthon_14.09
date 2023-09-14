from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CHOICES = (
        (1, 'admin'),
        (2, 'owner'),
        (3, 'user')
    )
    roles = models.PositiveSmallIntegerField(default=3, choices=CHOICES)
    phone_number = models.CharField(default='', max_length=20)