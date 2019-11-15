from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import student, subject, studentsPerSubject, sampleQuizzes, questions, reviewers
from django.contrib.auth.decorators import login_required
from pprint import pprint

# Create your views here.
def landing(request):
    return render(request, 'registration/landing.html')

def signup(request):
    if(request.method == 'POST'):
        try:
            newUsername = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            newEmail = request.POST.get('email')
            if(password1 == password2):
                newPassword = request.POST.get('password1')
                user = student.objects.create_user(username=newUsername, password=newPassword, email=newEmail)
                messages.success(request, f'Account created!')
                # return render(request, "registration/signup.html")
                return redirect('login_user')

            else:
                messages.error(request, 'Error passwords did not match each other')
                return render(request, 'registration/signup.html')

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            messages.error(request, 'Error please input valid values for each field')
            return render(request, 'registration/signup.html')
    else:
        return render(request, 'registration/signup.html')

def login_user(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(username=username, password=password)

        if (user is not None):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please enter a valid username-password combination')
            return render(request, "registration/login.html")

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')

@login_required
def home(request):
    user=request.user

    userSubjects = studentsPerSubject.objects.filter(student=user)

    pprint(userSubjects)
    return render(request, 'registration/home.html', {'subjects':userSubjects})

@login_required
def showSubject(request, subject_id):
    user=request.user
    specifiedSubject = subject.objects.get(id=subject_id)
    reviewerList = reviewers.objects.filter(subject=specifiedSubject)

    return render(request, 'registration/subjectPage.html', {'subject':specifiedSubject, 'reviewers': reviewerList})

@login_required
def showReviewer(request, reviewer_id):
    user=request.user
    specifiedReviewer = reviewers.objects.get(reviewerId=reviewer_id)
    try:
        quiz = sampleQuizzes.objects.get(reviewer=specifiedReviewer)
    except sampleQuizzes.DoesNotExist:
        quiz = None

    print(quiz)

    return render(request, 'registration/reviewerPage.html', {'reviewer':specifiedReviewer, 'quiz':quiz})

@login_required
def showAllReviewers(request):
    userSubjects = []
    user=request.user
    userClasses = studentsPerSubject.objects.filter(student=user)

    for x in userClasses:
        userSubjects.append(x.subject)

    allReviewers = reviewers.objects.filter(subject__in=userSubjects)

    return render(request, 'registration/allReviewers.html', {'reviewers':allReviewers})

@login_required
def createReviewer(request, subject_id):
    if(request.method == 'POST'):
        title = request.POST.get('title')
        content = request.POST.get('content')
        specifiedSubject = subject.objects.get(id=subject_id)

        reviewer = reviewers.objects.create(subject=specifiedSubject, reviewerTitle=title, reviewerContent=content)

        return showAllReviewers(request)
    return render(request, 'registration/createReviewer.html')


@login_required
def createClass(request):
    if(request.method == 'POST'):
        subjectTitle = request.POST.get('classnumber')
        subjectName = request.POST.get('classname')
        classCode = request.POST.get('classcode')

        createdSubject = subject.objects.create(subjectTitle=subjectTitle, subjectName=subjectName, classCode=classCode)
        joinClass = studentsPerSubject.objects.create(student=request.user, subject=createdSubject)

        return home(request)
    return render(request, 'registration/createClass.html')

@login_required
def joinClass(request):
    if(request.method == 'POST'):
        subjectTitle = subject.objects.get(subjectTitle=request.POST.get('classnumber'))
        subjectName = request.POST.get('classname')
        classCode = request.POST.get('classcode')
        if((subjectTitle.subjectName == subjectName) and (subjectTitle.classCode == classCode)):
            joinClass = studentsPerSubject.objects.create(student=request.user, subject=createdSubject)
        return home(request)
    return render(request, 'registration/joinClass.html')

@login_required
def openQuiz(request, reviewer_id, quiz_id):
    if(request.method == 'POST'):
        choice = request.POST.get('qtype')
        if(choice == "multiple_choice"):
            return redirect('multipleChoice', reviewer_id=reviewer_id, quiz_id=quiz_id)
            # return render(request, 'registration/multipleChoice.html', {'reviewerId': reviewer_id, 'quizId': quiz_id})
        elif(choice == 'short_answer'):
            return redirect('shortAnswer', reviewer_id=reviewer_id, quiz_id=quiz_id)

    sampleQuiz = sampleQuizzes.objects.get(quizId=quiz_id)
    items = questions.objects.filter(quizId=quiz_id)
    return render(request, 'registration/quizPage.html', {'quiz':sampleQuiz, 'items':items})

@login_required
def quizTitle(request, reviewer_id):
    if(request.method == 'POST'):
        quiz = request.POST.get('quiztitle')
        reviewer = reviewers.objects.get(reviewerId=reviewer_id)
        sampleQuizzes.objects.create(reviewer=reviewer, quizTitle=quiz)
        return showReviewer(request, reviewer_id)
    return render(request, 'registration/quizTitle.html')

@login_required
def multipleChoice(request, reviewer_id, quiz_id):
    if(request.method == 'POST'):
        questionType = "multiple choice"
        questionText = request.POST.get('questionA')
        choiceA = request.POST.get('choiceA')
        choiceB = request.POST.get('choiceB')
        choiceC = request.POST.get('choiceC')
        choiceD = request.POST.get('choiceD')
        answer = request.POST.get('answer')
        quiz = sampleQuizzes.objects.get(quizId=quiz_id)
        questions.objects.create(quizId=quiz, questionType=questionType, questionText=questionText, choiceA=choiceA, choiceB=choiceB, choiceC=choiceC, choiceD=choiceD, answer=answer)

        sampleQuiz = sampleQuizzes.objects.get(quizId=quiz_id)
        items = questions.objects.filter(quizId=quiz_id)
        return redirect('openQuiz', reviewer_id=reviewer_id, quiz_id=quiz_id)
    else:
        return render(request, 'registration/multipleChoice.html')

@login_required
def shortAnswer(request, reviewer_id, quiz_id):
    if(request.method == 'POST'):
        questionType = "short answer"
        questionText = request.POST.get('questionA')
        answer = request.POST.get('answerA')
        quiz = sampleQuizzes.objects.get(quizId=quiz_id)
        questions.objects.create(quizId=quiz, questionType=questionType, questionText=questionText, answer=answer)

        sampleQuiz = sampleQuizzes.objects.get(quizId=quiz_id)
        items = questions.objects.filter(quizId=quiz_id)
        return redirect('openQuiz', reviewer_id=reviewer_id, quiz_id=quiz_id)
    else:
        return render(request, 'registration/shortAnswer.html')
