
from django.utils.html import mark_safe
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Items(models.Model):
    title = models.CharField('Названия', max_length=50)
    short_description = models.CharField('Краткое описание', max_length=150)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    image = models.ImageField(default = 'noimage.jpg', upload_to = 'image')
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.title

    


class Comment(models.Model):
    text = models.CharField('Текст комментария', max_length=150)
    user_nickname = models.CharField('Ник пользователя', max_length=10)
    comment_date = models.DateTimeField('Дата комментария')
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
    def __str__(self):
        return f"Комментарий: {self.text}, Время: {self.comment_date}, ник: {self.user_nickname}"
    
    def get_absolute_url(self):
        return f'/shop/comments/{self.id}'


class Comments(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='Comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    text = models.CharField('Текст комментария', max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Комментарий123'
        verbose_name_plural = 'Комментарии123'
        ordering = ('created',)

    def __str__(self):
        return 'Comment on {}'.format(self.item)


    


