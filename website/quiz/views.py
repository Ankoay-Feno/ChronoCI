from django.shortcuts import render, get_object_or_404
from .models import Question

def quiz(request):
    questions = Question.objects.all()
    return render(request, "quiz/quiz.html", {"questions": questions})

def result(request):
    if request.method == "POST":
        score = 0
        total = Question.objects.count()

        for question in Question.objects.all():
            selected_choice = request.POST.get(str(question.id))
            if selected_choice:
                choice = question.choices.get(id=int(selected_choice))
                if choice.is_correct:
                    score += 1

        return render(request, "quiz/result.html", {"score": score, "total": total})

    return render(request, "quiz/quiz.html")
