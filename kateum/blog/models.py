from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    # content = models.TextField(blank=True)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    num_likes = models.ManyToManyField(User, related_name="blog_posts")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)

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
        ordering = ['id']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']