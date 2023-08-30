from django.shortcuts import render

from django.http import HttpResponse

def quizzes(request):
    return HttpResponse("Hello quizz world!")
