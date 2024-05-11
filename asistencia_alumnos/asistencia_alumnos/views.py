from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def home(request):
    tempates_name='home.html'
    return render(request, tempates_name, {})