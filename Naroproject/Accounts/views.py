from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
# Djanog에서 제공하는 회원가입 Form
from django.contrib.auth.forms import UserCreationForm
import random

def signup(request):
    # request 방식이 POST이면 
    signup_form = SignUpForm()
    if request.method == "POST":
        # email 추출
        [email] = dict(request.POST)['email']
        # POST일때 객체 생성
        signup_form = SignUpForm(request.POST)
        # 해당 폼의 유효성 검사가 유효하면 user_instance에 signup_form을 저장한다.
        if signup_form.is_valid():
            # 하지만 아래에서 또 한번 저장이 있으므로  중복 저장을 피하기 위해 commit=Flase
            user_instance = signup_form.save(commit = False)
            # Set_password 및 cleaned_data를 통해 유효한 문자만 남긴 상태를 저장한다. 또한 암호화한다.
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()
            # render 뒤쪽에 {'username':user_instance.username}을 넣어서 username이 나오도록 구현해준다.
            item = User.objects.get(email=email)
            randomvalue = random.randint(1, 1000)
            nickname = "나로 " + str(randomvalue) + "호"
            item.nickname = nickname
            item.save()
            # redirect를 해주는 게 맞는데 아이디를 전달하게 되면서 redirect는 딕셔너리 데이터를 전달해줄 수가 없어여 차피 나중에 alert 뺄 것 같으니 이렇게 넣어 놓겠습니다 ㅎㅎ
            # return redirect('login')
            return render(request, 'registration/login.html', {'id': nickname})
        else:
            signup_form = SignUpForm(request.POST)
    return render(request, 'registration/signup.html', {'form':signup_form.as_p})