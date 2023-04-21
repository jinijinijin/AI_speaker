from django.shortcuts import render

def index(request):
    return render(
        request,
        'main/index.html',
    )

def question(request):
    return render(
        request,
        'main/question.html',
    )

def result(request):
    return render(
        request,
        'main/result.html',
    )

def login(request):
    return render(
        request,
        'main/login.html',
    )
