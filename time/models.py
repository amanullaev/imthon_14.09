from django.db import models


class BornModel(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.title