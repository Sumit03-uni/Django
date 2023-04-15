from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def home(request):
    if request.user.is_anonymous:
      return redirect('/loginUser')
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html',)

def service(request):
    return render(request, 'service.html',)

def contact(request):
   if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    contact = Contact(name=name, email=email, subject=subject, message=message, date= datetime.today())
    contact.save()
    messages.success(request, 'Your message has been sent!')
   return render(request, 'contact.html',)

def blog(request):
   return render(request, 'blog.html',)

def price(request):
   return render(request, 'price.html',)

def feature(request):
   return render(request, 'feature.html',)

def detail(request):
   return render(request, 'detail.html',)

def quote(request):
   return render(request, 'quote.html',)

def team(request):
   return render(request, 'team.html',)

def testimonial(request):
   return render(request, 'testimonial.html',)

# def loginUser(request):
#    return render (request, 'login.html',)

def loginUser(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('/')

      else:
         messages.warning(request, 'Incorret username or Password!')
         return render(request, 'loginUser.html')
   return render(request, 'loginUser.html')

def logoutUser(request):
   logout(request)
   return redirect('/loginUser')

