from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question, Quiz
from int_question.models import Int_Question

from .forms import MyIntForm
from club.models import ExamEvent

from random import shuffle

def pre_quiz(request,slug):
    request.session.set_expiry(3600)
    quiz = Quiz.objects.get(url = slug)
    request.session['quiz'] = quiz.id
    q_list = list(Int_Question.objects.filter(quiz = quiz))

    shuffle(q_list) #always!

    qn_list = [x.id for x in q_list]
    request.session['qn_list'] = qn_list
    cor_list = [x.correct for x in q_list]
    request.session['cor_list'] = cor_list

    n = len (qn_list)

    ans_list = [None]*n
    request.session['ans_list'] = ans_list

    qs = quiz

    request.session['current'] = 0

    return render(request,'pre_quiz.html',
                {'qs':qs,
                })

def exam_prev(request):
    return exam(request, -1)

def exam_next(request):
    return exam(request,1)

def exam(request, shift = 0):
    qz = request.session.get('quiz')
    quiz = Quiz.objects.get(id = qz)

    qn_list = request.session.get('qn_list')

    n = len (qn_list)

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
                {'current':current+1,
                    'n':n,
                    'question':q,
                    'form': form,
                    'quiz':quiz
                })

def pre_final(request):
    ans_list = request.session.get('ans_list')
    cor_list = request.session.get('cor_list')
    current = request.session.get('current')

    n = len(ans_list)
    mis_list = []

    for i in range(n):
        if ans_list[i] is None:
            mis_list.append([True,i+1])
        else:
            mis_list.append([False,i+1])

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
