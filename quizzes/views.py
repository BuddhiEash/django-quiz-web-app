from django.shortcuts import render

from django.http import HttpResponse

def quizz_view(request):
    return HttpResponse("Hello quizz world!")
