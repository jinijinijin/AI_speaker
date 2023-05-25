from django.shortcuts import render
from .models import User
from django.http import HttpResponse


#def index(request):
#    return render(request, 'main/index.html')


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

from django.shortcuts import render, redirect
from .forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 로그인 처리
            login_name = form.cleaned_data['login_name']
            login_phone_number = form.cleaned_data['login_phone_number']
            # 여기서 로그인 처리를 구현하면 됩니다.
            # 유효한 로그인인지 검증하고 성공하면 로그인 성공 페이지로 리다이렉트할 수 있습니다.
            return redirect('sign')
    else:
        form = LoginForm()
    return render(request, 'main/index.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        # 회원가입 처리
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        # 여기서 회원가입 처리를 구현하면 됩니다.
        # 회원가입이 완료되면 회원가입 성공 페이지로 이동할 수 있습니다.
        return redirect('sign')
    return render(request, 'main/login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login_name')
        password = request.POST.get('login_phone_number')

        if not username or not password:
            error_message = "이름과 전화번호를 모두 입력해주세요."
            return render(request, 'main/login.html', {'error_message': error_message})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 로그인 후 리다이렉트할 URL
        else:
            error_message = "유효하지 않은 사용자 이름 또는 비밀번호입니다."
            return render(request, 'main/login.html', {'error_message': error_message})

    return render(request, 'main/login.html')


def result(request):
    return render(request, 'main/result.html')