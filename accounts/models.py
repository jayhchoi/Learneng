from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_member = models.BooleanField(_('멤버'), default=False)
    is_leader = models.BooleanField(_('리더'), default=False)
    email = models.EmailField(_('이메일'), unique=False) # set to true later
    name = models.CharField(_('이름'), max_length=30)
    contact = models.CharField(_('연락처'), null=True, blank=True, max_length=120)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(_('자기소개'))
    photo = models.ImageField(_('프로필 사진'), upload_to='accounts/%Y/%m/%d/',
                                        default='default/profile-default.jpg')

    def __str__(self):
        return self.user.username

    def get_average_rating(self):
        comment_qs = self.user.comment_to.all()
        total_rating = 0
        for comment in comment_qs:
            total_rating += comment.rating
        if comment_qs.count():
            average_rating = total_rating / comment_qs.count()
        else:
            average_rating = 0
        return round(average_rating, 2)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    profile, created = Profile.objects.get_or_create(user=instance)
    print(created)
    profile.save()