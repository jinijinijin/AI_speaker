from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def main(request):
    return render(request, 'main/main.html')


def questions(request):
    return render(request, 'main/question.html')


def sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')

        if not name or not phone_number:
            error_message = "이름과 전화번호를 모두 입력해주세요."
            return HttpResponse(f'<script>alert("{error_message}"); history.go(-1);</script>')

        user = User(name=name, phone_number=phone_number)
        user.save()
        return render(request, 'main/login.html')  # 회원가입 성공 페이지로 이동

    return render(request, 'main/login.html')


def result(request):
    return render(request, 'main/result.html')