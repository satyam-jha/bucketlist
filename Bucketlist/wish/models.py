from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.


class wishes(models.Model):
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default=True)
    wish_tittle = models.CharField(max_length=200)
    wish_description = models.TextField()
    wish_status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())
    completed = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "wish"

    def __str__(self):
        return self.wish_tittle
