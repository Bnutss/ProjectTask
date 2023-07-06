from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Малый'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    STATUS_CHOICES = [
        ('not_completed', 'Не выполнено'),
        ('completed', 'Выполнено'),
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    deadline = models.DateField(verbose_name='Крайний срок')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, verbose_name='Уровень приоритета')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_completed', verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_date', 'title']

