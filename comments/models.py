from django.db import models
from django.conf import settings


RATING_CHOICES = (
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
)

class Comment(models.Model):
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_to')
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_by')
    body = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return "from " + self.member.username + " to " + self.leader.username

    def get_star_checked(self):
        return "x" * self.rating

    def get_star_unchecked(self):
        return "x" * (5 - self.rating)
