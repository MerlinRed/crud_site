from django.db import models


# Create your models here.

class Task(models.Model):
    text = models.TextField('Текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
