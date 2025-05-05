from django.urls import path
from .views import quiz, result

urlpatterns = [
    path("", quiz, name="quiz"),
    path("result/", result, name="result"),
]
