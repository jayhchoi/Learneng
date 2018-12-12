from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_student = models.BooleanField(_('student'), default=False)
    is_teacher = models.BooleanField(_('teacher'), default=False)
    email = models.EmailField(_('email address'), unique=False) # set to true later
    name = models.CharField(_('full name'), max_length=30)
    contact = models.CharField(_('contact'), null=True, blank=True, max_length=120)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/%Y/%m/%d/',
                                        default='default/profile-default.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    profile, created = Profile.objects.get_or_create(user=instance)
    print(created)
    profile.save()