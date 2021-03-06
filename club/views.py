from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from quiz.models import Sitting, Quiz
from .models import NewsRecord, ExamEvent, MagicNode

from collections import Counter
from operator import itemgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def topic_tree(request,id):
    get = lambda node_id: MagicNode.objects.get(pk=node_id)
    try:
        node = get(id)
    except:
        node = MagicNode.get_first_root_node()

    if node.is_root():
        node = node.get_first_child()    

    children = node.get_children()
    parent = node.get_parent()
    siblings = node.get_siblings()

    return render(request,'topic_tree.html',
                    {'node':node,
                     'children':children,
                     'parent':parent,
                     'siblings':siblings,
                     })

def topic_search(request):
    return render(request,'topic_search.html',
                    { })

def score(quiz,user):
    qs = ExamEvent.objects.filter(quiz = quiz, user = user)
    m = 0
    for x in qs:
        if x.result > m:
            m = x.result
    return m

class MyQuizScore:
    def __init__(self,quiz,user):
        self.user = user
        self.score = score(quiz,user)
        self.name = quiz.title
        self.slug = quiz.url
        sc = self.score
        if  sc == 0:
            color = " "
            p = "pawn"
        elif 0 < sc < 30:
            color = "btn-primary btn-danger"
            p = "knight"
        elif 30 <= sc < 60:
            color = "btn-primary btn-warning"
            p = "bishop"
        elif 60 <= sc < 85:
            color = "btn-primary btn-success"
            p = "tower"
        elif 85 <= sc < 100:
            color = "btn-primary btn-info"
            p = "queen"
        else:
            color = "btn-primary btn-primary"
            p = "king"

        self.color = color
        self.piece = p

def map(request):
    qs1 = Quiz.objects.filter(draft=False)
    qs = [MyQuizScore(x,request.user) for x in qs1]

    return render(request,'map.html',
                {'qs':qs,
                })

def quiz_table(request):
    qs = list(Quiz.objects.filter(draft=False))
    qq = []
    for i in range(len(qs)):
        x = qs[i]
        qq.append([x,score(x, request.user),i+1])

    return render(request,'quiz_table.html',
                {'qq':qq,
                })

def news(request):
    x_list = NewsRecord.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(x_list, 10)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    return render(request,'news.html',
            {'qs':qs,
            })

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def password_change_done(request):
    return msg(request, 'Your password was changed successfully!')

def password_reset_done(request):
    return msg(request, 'Your password was changed successfully!')

def hard_quiz(request):
    qq = list(Quiz.objects.filter(draft=False))
    qs = set()
    ks = ExamEvent.objects.all()

    for exam in ks:
        if exam.result >= 99:
            pair = (exam.user,exam.quiz)
            qs.add(pair)

    qz_done_cases = [quiz for user,quiz in qs]
    dic = Counter(qz_done_cases)

    for x in qq:
        if x not in dic:
            dic[x]=0

    quiz_done_list = sorted(dic.items(), key=itemgetter(1))

    tab = []
    for i in range(len(quiz_done_list)):
        t = [quiz_done_list[i][0],quiz_done_list[i][1],i+1]
        tab.append(t)

    return render(request,'hard_quiz.html',
        {'qzs':tab,
        })

def other(request):
    qq = list(Quiz.objects.filter(draft=False))
    nq = len(qq)

    qs = set()
    if not request.user.is_anonymous:
        ks = ExamEvent.objects.all()

        for exam in ks:
            if exam.result >= 99:
                pair = (exam.user,exam.quiz)
                qs.add(pair)

    qz_done_cases = [user for user,quiz in qs]
    dic = Counter(qz_done_cases)
    user_done_list = sorted(dic.items(), key=itemgetter(1), reverse = True)

    tab = []
    for i in range(len(user_done_list)):
        t = [user_done_list[i][0],user_done_list[i][1],i+1,100*user_done_list[i][1]//nq]
        tab.append(t)

    return render(request,'other.html',
        {'qzs':tab,
        })

def other_old(request):
    qs = set()
    if not request.user.is_anonymous:
        ks = Sitting.objects.all()

        for x in ks:
            if x.check_if_passed:
                y = (x.user,x.quiz)
                qs.add(y)

    q1 = [x for x,y in qs]
    d = Counter(q1)
    q2 = sorted(d.items(), key=itemgetter(1), reverse = True)

    q3 = []
    for i in range(len(q2)):
        t = [q2[i][0],q2[i][1],i+1]
        q3.append(t)

    return render(request,'other.html',
        {'qzs':q3,
        })

def index(request):
    news = NewsRecord.objects.all()[:1].get()

    qzs = set()
    if not request.user.is_anonymous:
        ks = Sitting.objects.all().filter(user = request.user)

        for x in ks:
            if x.check_if_passed:
                qzs.add(x.quiz)

    form = AuthenticationForm(request)
    return render(request,'index.html',
        {'form':form,'qzs':qzs, 'news':news
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
