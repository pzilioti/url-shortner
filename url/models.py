from django.db import models


class Url(models.Model):
    short = models.CharField(max_length=5)
    long = models.CharField(max_length=100)
    click_count = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['short'], name='unique_short_url'),
        ]

    def __str__(self):
        return f"URL {self.long} shortned to {self.short}. Accesed {self.click_count} times"
