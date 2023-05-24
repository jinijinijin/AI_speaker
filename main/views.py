from django.shortcuts import render


def index(request):
    return render(
        request,
        'main/index.html',

    )

def main(request):
    return render(
        request,
        'main/main.html',
    )

def questions(request):
    return render(
        request,
        'main/question.html',
    )

def login(request):
    return render(
        request,
        'main/login.html',
    )


def result(request):
    return render(
        request,
        'main/result.html',
    )



from django.http import HttpResponse

def question_view(request):
    # question.js 파일의 내용을 문자열로 읽어온다.
    with open('main/static/main/js/question.js', 'r') as file:
        question_js_content = file.read()

    # HttpResponse 객체를 생성하여 question.js 파일의 내용과 MIME 유형을 설정한다.
    response = HttpResponse(question_js_content)
    response['Content-Type'] = 'text/javascript'
    return response