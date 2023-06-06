
def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/main.html')

def questions1(request):
    return render(request, 'main/question1.html')
def questions2(request):
    return render(request, 'main/question2.html')
def questions3(request):
    return render(request, 'main/question3.html')
def questions4(request):
    return render(request, 'main/question4.html')
def questions5(request):
    return render(request, 'main/question5.html')
def questions6(request):
    return render(request, 'main/question6.html')
def questions7(request):
    return render(request, 'main/question7.html')


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
            user = User.objects.create_user(name=name, phone_number=phone_number)
            user.save()

            # 회원가입 성공 시 로그인 처리
            login(request, user)

            # 회원가입 및 로그인 성공 시 리다이렉트
            return redirect('index')  # or redirect('main:index')

        elif 'login' in request.POST:  # 로그인 요청인 경우
            login_name = request.POST['login_name']
            login_phone_number = request.POST['login_phone_number']

            user = authenticate(request, name=login_name, password=login_phone_number)
            if user is not None:
                login(request, user)
                # 로그인 성공 시 리다이렉트
                return redirect('index')  # or redirect('main:index')
            else:
                # 로그인 실패 시 처리할 내용
                return render(request, 'main/login.html', {'message': '로그인에 실패하였습니다.'})

    return render(request, 'main/login.html')


from .models import SurveyResponse

def survey_form_submit(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')


        survey_response = SurveyResponse(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10)
        survey_response.save()

        return redirect('main/result.html')  # Redirect to a thank you page or another appropriate page

    return render(request, 'main/sign.html')  # Render the survey form page if the request method is not POST
