from django.db import models


class QuestionM(models.Model):
    question_text = models.CharField(max_length=200)

class ChoiceM(models.Model):
    question_fk = models.ForeignKey(QuestionM, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    numberOfVotes = models.IntegerField(default=0)
