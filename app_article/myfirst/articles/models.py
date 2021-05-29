from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Atricle(models.Model):
    article_title=models.CharField("Название статьи",max_length=200)
    article_text=models.TextField("Текст статьи")
    pub_date=models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date>=(timezone.now()-datetime.timedelta(days=7))

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Atricle,on_delete=models.CASCADE)
    author_name=models.CharField("Имя автора",max_length=50)
    comment_text=models.CharField("Текст комметария",max_length=200)


    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'