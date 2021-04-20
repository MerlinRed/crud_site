from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    text = models.TextField('Текст')
    users_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
