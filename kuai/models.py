from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class Qa(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='qa')


    # def __str__(self):
    #     return self.category

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = 'Экзамены'
