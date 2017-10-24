from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question, Quiz
from int_question.models import Int_Question

from .forms import MyIntForm
from club.models import ExamEvent

def pre_quiz(request,slug):
    request.session.set_expiry(25920) #3 days/10
    quiz = Quiz.objects.get(url = slug)
    request.session['quiz'] = quiz.id
    q_list = Int_Question.objects.filter(quiz = quiz)
    qn_list = [x.id for x in q_list]
    request.session['qn_list'] = qn_list
    cor_list = [x.correct for x in q_list]
    request.session['cor_list'] = cor_list

    n = len (qn_list)

    ans_list = [None]*n
    request.session['ans_list'] = ans_list

    qs = slug

    return render(request,'pre_quiz.html',
                {'qs':qs,
                })

def exam_prev(request):
    return exam(request, -1)

def exam_next(request):
    return exam(request,1)

def exam(request, shift = 0):
    quiz = request.session.get('quiz')
    qn_list = request.session.get('qn_list')

    n = len (qn_list)

    if request.session.get('current') == None:
        current = request.session['current'] = 0
    else:
        current = request.session.get('current')

    if request.method == 'POST':
        form = MyIntForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            request.session['ans_list'][current] = answer

    current = (current + shift) % n
    request.session['current'] = current
    a = request.session.get('ans_list')[current]
    form = MyIntForm(initial = {'answer':a})
    q = Int_Question.objects.get(id = qn_list[current])

    return render(request,'exam.html',
                {'current':current,
                    'n':n,
                    'question':q,
                    'form': form
                })

def pre_final(request):
    ans_list = request.session.get('ans_list')
    cor_list = request.session.get('cor_list')
    current = request.session.get('current')

    n = len(cor_list)
    mis_list = [False]*n

    for i in range(n):
        if ans_list[i] is None:
            mis_list[i] = True

    return render(request,'pre_final.html',
                {'mis_list':mis_list,
                })

def final(request):
    ans_list = request.session.get('ans_list')
    cor_list = request.session.get('cor_list')
    current = request.session.get('current')
    quiz_id = request.session.get('quiz')

    quiz = Quiz.objects.get(id = quiz_id)

    n = len(ans_list)
    xi_list = []
    nn = 0

    for i in range(n):
        if ans_list[i] is None:
            xi_list.append([None,i+1])
        elif ans_list[i] == cor_list[i]:
            xi_list.append([True,i+1])
            nn += 1
        else:
            xi_list.append([False,i+1])

    r = (100 * nn) // n
    event = ExamEvent(user = request.user, result = r, quiz = quiz)
    event.save()

    return render(request,'final.html',
                {'xi_list':xi_list,
                })
