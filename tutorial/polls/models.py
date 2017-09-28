from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'설문조사 ({self.title})'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return f'{self.title} (설문:{self.question.title})'
