# Generated by Django 4.1.5 on 2023-01-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tool'),
        ),
    ]
