from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, blank=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
