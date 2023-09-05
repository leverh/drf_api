from django.db import models
from django.conf import settings


class UserBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="reading_list", through='UserBook')

    def __str__(self):
        return self.title
