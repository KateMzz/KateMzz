# Generated by Django 4.1.7 on 2023-04-11 23:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_remove_post_post_likes_remove_post_post_likes_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]