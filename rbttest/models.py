
from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=50)

class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    choice = models.CharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)