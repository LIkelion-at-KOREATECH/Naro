from django.shortcuts import render
from . models import Textmodel

# Create your views here.

def home(request):
    return render(request, 'main/main_bf_login.html')
    
def main_af_login(request):
    return render(request, 'main/main_af_login.html')

def answer(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        answer = Answer.objects.create(
            answer=answer,
        )
        return HttpResponse('POST method')
    elif request.method == 'GET':
        return render(request, 'main/main_af_login.html')