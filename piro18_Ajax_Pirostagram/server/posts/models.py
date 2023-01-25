from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    like = models.BooleanField(default=False, verbose_name='좋아요')