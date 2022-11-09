from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Document(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documents'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
