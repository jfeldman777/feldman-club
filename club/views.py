from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from quiz.models import Sitting

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def password_change_done(request):
    return msg(request, 'Your password was changed successfully!')

def password_reset_done(request):
    return msg(request, 'Your password was changed successfully!')

def index(request):
    qzs = set()
    if not request.user.is_anonymous:
        ks = Sitting.objects.all().filter(user = request.user)

        for x in ks:
            if x.check_if_passed:
                qzs.add(x.quiz)

    #print(qzs)

    form = AuthenticationForm(request)
    return render(request,'index.html',
        {'form':form,'qzs':qzs
        })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                User.objects.get(email = email)
                return msg(request,'This email is in DB, probably you have been registered')
            except:
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
