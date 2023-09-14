from django.db import models
from user_api.models import UserModel


class FieldModel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    is_indoor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name76d


class BookingModel(models.Model):
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.field.name} by {self.user.name}"



