from django.db import models
from django.utils import timezone

class Question(models.Model):
    id = models.CharField("id", max_length=10, primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=1000, default="")

    voting_closed = models.BooleanField("voting closed", default=False)
    closed_date = models.DateTimeField('close date', default=None, null=True)
    enable_closed_date = models.BooleanField("enable close date", default=False)

    def is_expired(self):
        return timezone.now() > self.closed_date

    def is_published(self):
        return timezone.now() > self.pub_date

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
