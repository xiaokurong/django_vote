from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Answer,QuestionNaire,Question,Investigator,InvestigateUserInfo,QuestionType
from django.db.models import F,Q
from django.db.models import Avg, Sum, Max, Min, Count


def vote_index(request):
    return render(request, 'vote/vote_index.html')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active :
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()

    return render(request,'vote/login.html',{'form':form})

def question(request):
    try:
        question_set = Question.objects.all()
        question_type_set = QuestionType.objects.all()
        return render(request, 'vote/question.html',{'question_set': question_set , 'question_type_set': question_type_set})
    except Question.DoesNotExist :
        return render(request,'vote/question.html',{'error': "数据库异常！"})



def investigator(request):
    try:
        investigator_set = Investigator.objects.all()
        return render(request,'vote/investigator.html',{'investigator_set': investigator_set})
    except Investigator.DoesNotExist :
        return render(request,'vote/investigator.html',{'error': '数据库异常！'})


def questionnaire(request):
    try:
        questionnaire_set = QuestionNaire.objects.annotate(queNum=Count('question__questionnaire')).values('id','title','queNum',)
        return render(request,'vote/questionnaire.html',{'questionnaire_set': questionnaire_set})
    except QuestionNaire.DoesNotExist :
        return render(request,'vote/questionnaire.html',{'error': '数据库异常！'})



def history(request):
    try:
        answer_set = Answer.objects.all()
        question_set = Question.objects.all()
        investigator_set = InvestigateUserInfo.objects.all()
        investigateuser_set = Investigator.objects.all()
        question_type_set = QuestionType.objects.all()

        return render(request,'vote/history.html',{'answer_set': answer_set,'question_set': question_set,'investigator_set':investigator_set,'investigateuser_set':investigateuser_set,'question_type_set':question_type_set})
    except Answer.DoesNotExist :
        return render(request,)

    return render(request,'vote/history.html')

def investigateuser(request):
    try:
        investigateuser_set = InvestigateUserInfo.objects.all()

        return render(request,'vote/investigateuser.html',{'investigateuser_set': investigateuser_set})
    except InvestigateUserInfo.DoesNotExist :
        return render(request,'vote/investigateuser.html',{'error': '数据库异常！'})



def other(request):
    return render(request,'vote/other.html')