from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/question.html', context)


def vote(request, pk):
    if request.POST:
        try:
            choice_pk = request.POST['vote']
        except Question.DoesNotExist:
            return redirect('index')
        except MultiValueDictKeyError:
            pass
        try:
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        except Choice.DoesNotExist:
            pass
        return redirect('question_detail', pk=pk)
    return HttpResponse(status=404)
