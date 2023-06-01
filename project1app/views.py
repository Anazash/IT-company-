from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    return render(request,'services.html')

def signup(request):
    return render(request,'signup.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

