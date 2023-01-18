from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="아이디어명")
    content = models.TextField(verbose_name="아이디어설명")
    interest = models.IntegerField(verbose_name="아이디어관심도")
    devtool = models.CharField(max_length=50, verbose_name="예상개발툴")
    # 저장경로: MEDIA_ROOT/posts/20230117/xxx.png
    # DB필드: 'MEDIA_URL/posts/20230117/xxx.png'라는 문자열 저장
    photo = models.ImageField(null=True, blank=True, upload_to='posts/%Y%m%d')

class Tool(models.Model):
    content = models.TextField(verbose_name="개발툴설명")
    name = models.CharField(null=True, max_length=50, verbose_name="이름")
    kind = models.CharField(null=True, max_length=50, verbose_name="종류")
