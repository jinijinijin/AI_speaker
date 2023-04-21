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
