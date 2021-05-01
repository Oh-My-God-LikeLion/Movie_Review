from __future__ import unicode_literals  # 문자 인코딩
from django.utils import timezone
from django.db import models


# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)  # 등록 시점
    review = models.TextField(default='')

    plot = models.TextField(default='')
    release_date = models.DateField()
    # poster = models.ImageField(upload_to="posters")

    action = '액션'
    thriller = '스릴러'
    romance = '로맨스'
    comdedy = '코미디'
    musical = '뮤지컬'
    fantasy = '판타지'
    animation = '애니메이션'
    GENRE_CHOICES = [
        (action, '액션'),
        (thriller, '스릴러'),
        (romance, '로맨스'),
        (comdedy, '코미디'),
        (musical, '뮤지컬'),
        (fantasy, '판타지'),
        (animation, '애니메이션'),
    ]
    genre = models.CharField(
        max_length=10,
        choices=GENRE_CHOICES,
        default=action
    )
    score = models.IntegerField(default=0)
