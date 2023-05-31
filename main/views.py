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

from django.contrib.auth.models import User


from django.shortcuts import render, redirect


from .models import User
from django.contrib.auth import authenticate, login

def login_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:  # 회원가입 요청인 경우
            name = request.POST['name']
            phone_number = request.POST['phone_number']

            # 중복 여부 체크
            if User.objects.filter(name=name).exists():
                return render(request, 'main/login.html', {'message': '이미 존재하는 사용자입니다.'})

            # 사용자 생성
            user = User(name=name, phone_number=phone_number)
            user.save()

            # 회원가입 성공 시 로그인 처리
            login(request, user)

            # 회원가입 및 로그인 성공 시 리다이렉트
            return redirect('login')  # or redirect('main:index')

        elif 'login' in request.POST:  # 로그인 요청인 경우
            login_name = request.POST['login_name']
            login_phone_number = request.POST['login_phone_number']

            user = authenticate(request, username=login_name, password=login_phone_number)
            if user is not None:
                login(request, user)
                # 로그인 성공 시 리다이렉트
                return redirect('index')  # or redirect('main:index')
            else:
                # 로그인 실패 시 처리할 내용
                return render(request, 'main/login.html', {'message': '로그인에 실패하였습니다.'})

    return render(request, 'main/login.html')