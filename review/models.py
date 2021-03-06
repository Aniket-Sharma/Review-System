from django.db import models

class Review(models.Model):
    RATING_CHOICES={(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=1500, null=True, blank=True)

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
