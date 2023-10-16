from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II'),
        ('amaro', 'Amaro'),
        ('mayfair', 'Mayfair'),
        ('perpetua', 'Perpetua'),
        ('willow', 'Willow'),
        ('aden', 'Aden'),
        ('brooklyn', 'Brooklyn'),
        ('clarendon', 'Clarendon'),
        ('gingham', 'Gingham'),
        ('moon', 'Moon'),
        ('reyes', 'Reyes'),
        ('slumber', 'Slumber'),
        ('stinson', 'Stinson'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()
