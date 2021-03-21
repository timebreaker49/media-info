from django.db import models


# Create your models here.

class Media(models.Model):
    artist = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    played_at = models.DateTimeField()
    href = models.CharField(max_length=500)

    # image
    def __str__(self):
        return self.artist
