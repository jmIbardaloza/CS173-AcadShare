from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class student(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharFeld(max_length=20)
    password = models.CharFeld(max_length=20)
    email = models.CharFeld(max_length=20)

    def __str__(self):
        return self.username

class subject(models.Model):
    id = models.AutoField(primary_key=True)
    subjectTitle = models.CharField(max_length=20)
    subjectName = models.CharField(max_length=50)
    classCode = models.CharField(max_length=50)

    def __str__(self):
        return self.subjectTitle

class studentsPerSubject(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE, related_name = "students")
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, related_name = "subjects")

    def __str__(self):
        return self.student.username

class reviewers(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, related_name = "reviewerSubject")
    reviewerId = models.AutoField(primary_key=True)
    reviewerTitle = models.CharField(max_length=100)
    reviewerFile = models.FileField(upload_to='Desktop/', blank=True)
    reviewerContent = models.CharField(max_length=99999, null=True)

    def __str__(self):
        return self.reviewerTitle

class sampleQuizzes(models.Model):
    reviewer = models.ForeignKey(reviewers, on_delete=models.CASCADE, related_name = "reviewerQuiz")
    quizId = models.AutoField(primary_key=True)
    quizTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.quizTitle

class questions(models.Model):
    quizId = models.ForeignKey(sampleQuizzes, on_delete=models.CASCADE, related_name = "quizzes")
    questionId = models.AutoField(primary_key=True)
    questionType = models.CharField(max_length=1000)
    questionText = models.CharField(max_length=1000)
    choiceA = models.CharField(max_length=1000, null=True)
    choiceB = models.CharField(max_length=1000, null=True)
    choiceC = models.CharField(max_length=1000, null=True)
    choiceD = models.CharField(max_length=1000, null=True)
    answer = models.CharField(max_length=1000, null=True)

    def __repr__(self):
        return self.quizId
