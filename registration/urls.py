"""AcadShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login_user'),
    path('home/', views.home, name='home'),
    path('home/subjects/<int:subject_id>/', views.showSubject, name='showSubject'),
    path('home/reviewers/<int:reviewer_id>/', views.showReviewer, name='showReviewer'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_user'),
    path('reviewers/', views.showAllReviewers, name='reviewers'),
    path('home/subjects/<int:subject_id>/createReviewer/', views.createReviewer, name='createReviewer'),
    path('createClass/', views.createClass, name='createClass'),
    path('joinClass/', views.joinClass, name='joinClass'),
    path('home/reviewers/<int:reviewer_id>/quizTitle', views.quizTitle, name='quizTitle'),
    path('home/reviewers/<int:reviewer_id>/quiz/<int:quiz_id>', views.openQuiz, name='openQuiz'),
    path('home/reviewers/<int:reviewer_id>/quiz/<int:quiz_id>/multiple_choice', views.multipleChoice, name='multipleChoice'),
    path('home/reviewers/<int:reviewer_id>/quiz/<int:quiz_id>/short_answer', views.shortAnswer, name='shortAnswer'),
]
