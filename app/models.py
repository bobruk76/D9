from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, blank=True, related_name='posts')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'

    def __str__(self):
        return f'{self.title}'