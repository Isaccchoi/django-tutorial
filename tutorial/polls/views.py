from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    choices = Choice.objects.filter(question=question)
    context = {
        'question': question,
        'choices': choices,
    }

    return render(request, 'polls/question.html', context)