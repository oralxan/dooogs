from django.db import models

class Post(models.Model):
    title = models.CharField(
        'название поста',
        max_length=128
    )
    description = models.TextField(
        'описание поста',
        blank=True,
        null=True
    )
    image = models.ImageField(
        'фото',
        upload_to='posts-images/'

    )
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'постc'