from django.shortcuts import render,redirect
from .models import form

# Create your views here.
def index(request):
    return render(request,'intro/index.html')

def exp(request):
    return render(request,'intro/exp.html')

def portfolio(request):
    return render(request,'intro/portfolio.html')

def about(request):
    return render(request,'intro/about.html')

def submit(request):
    a = request.GET
    first_name = a.get('first_name')
    last_name = a.get('last_name')
    mail = a.get('mail')
    phone = a.get('phone')
    text = a.get('text')

    case = form.objects.create(first_name=first_name,last_name=last_name,mail=mail,phone=phone,text=text)
    case.save()
    data = form.objects.all().order_by('-id')
    return render(request,'submit.html')