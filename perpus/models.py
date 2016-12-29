from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    id_book = models.CharField(max_length=200)
    pic_book = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    summary = models.TextField(null=True)


    def publish(self):
        self.created_date(timezone.now)
        self.save()

    def __str__(self):
        return self.title
