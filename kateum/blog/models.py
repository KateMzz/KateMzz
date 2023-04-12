from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
# Create your models here.

class Post(models.Model):
    # class NewManager(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(status='published')
    #
    # options = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # )

    title = models.CharField(max_length=150)
    # content = models.TextField(blank=True)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    # objects = models.Manager()
    # newmanager = NewManager()
    post_likes = models.ManyToManyField(User, related_name='likes', default=None, blank=True)
    post_likes_count = models.BigIntegerField(default='0')


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['pk']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

