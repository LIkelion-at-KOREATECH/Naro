from django.shortcuts import render, redirect

# Djanog에서 제공하는 회원가입 Form
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    regi_form = UserCreationForm()
    # request 방식이 POST이면 
    if request.method == "POST":
        filled_form = UserCreationFrom(request.POST)
        # 해당 폼의 유효성 검사가 유효하면 login 페이지로 연결한다.
        if filled_form.is_valid():
            filled_form.save()
            return redirect('login')
    return render(request, 'signup.html', {'regi_form':regi_form})