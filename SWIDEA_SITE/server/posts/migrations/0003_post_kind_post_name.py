# Generated by Django 4.1.5 on 2023-01-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kind',
            field=models.CharField(max_length=50, null=True, verbose_name='종류'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='이름'),
        ),
    ]
