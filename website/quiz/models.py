from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)  # Texte de la question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)  # Texte de la réponse
    is_correct = models.BooleanField(default=False)  # Vrai si c'est la bonne réponse
