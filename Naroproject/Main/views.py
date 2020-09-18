from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/main_bf_login.html')
    
def main_af_login(request):
    return render(request, 'main/main_af_login.html')