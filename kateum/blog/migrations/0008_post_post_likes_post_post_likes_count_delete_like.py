# Generated by Django 4.1.7 on 2023-04-11 21:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_remove_post_likes_like'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='Like',
        ),
    ]