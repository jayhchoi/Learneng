from django.db import models
from django.conf import settings
from django.urls import reverse


LEVEL_CHOICES = (
    ('초급', '초급'),
    ('중급', '중급'),
    ('고급', '고급')
)

DAY_CHOICES = (
    ('월요일', '월요일'),
    ('화요일', '화요일'),
    ('수요일', '수요일'),
    ('목요일', '목요일'),
    ('금요일', '금요일'),
    ('토요일', '토요일'),
    ('일요일', '일요일')
)

STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('full', 'Full')
)


class Group(models.Model):
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leader_of')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='member_of')
    name = models.CharField('스터디명', max_length=140)
    photo = models.ImageField('메인 이미지', upload_to='groups/%Y/%m/%d/',
                              default='default/group-default.jpg')
    level = models.CharField('레벨', max_length=30, choices=LEVEL_CHOICES, default='elementary')
    start_date = models.DateField('시작일')
    day = models.CharField('요일', max_length=30, default='토요일', choices=DAY_CHOICES)
    time = models.CharField('시간', max_length=30)
    duration = models.PositiveSmallIntegerField('기간(주)', default=4)
    price = models.PositiveSmallIntegerField('참여비(만원)', default=0)
    size = models.PositiveSmallIntegerField('최대정원', default=4)
    location = models.CharField('지역', max_length=30)
    description = models.TextField('스터디 소개')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=40, default='active', choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'pk': self.pk})


# class GroupMember(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


RATING_CHOICES = (
    (5, 5),
    (4, 4),
    (3, 3),
    (2, 2),
    (1, 1),
)


class Comment(models.Model):
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_to')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_by')
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return str(self.rating) + " by " + str(self.user)