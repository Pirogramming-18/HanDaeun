# Generated by Django 4.1.5 on 2023-01-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y%m%d'),
        ),
    ]
