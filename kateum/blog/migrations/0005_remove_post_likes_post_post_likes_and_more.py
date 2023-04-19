# Generated by Django 4.1.7 on 2023-04-11 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_rename_num_likes_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='n_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes_count',
            field=models.BigIntegerField(default='0'),
        ),
    ]