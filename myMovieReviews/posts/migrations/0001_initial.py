# Generated by Django 4.1.5 on 2023-01-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('year', models.IntegerField(verbose_name='개봉 연도')),
                ('genre', models.CharField(max_length=20, verbose_name='장르')),
                ('star', models.IntegerField(verbose_name='별점')),
                ('running', models.IntegerField(verbose_name='러닝타임')),
                ('review', models.TextField(verbose_name='리뷰')),
                ('director', models.CharField(max_length=50, verbose_name='감독')),
                ('actor', models.CharField(max_length=50, verbose_name='배우')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]