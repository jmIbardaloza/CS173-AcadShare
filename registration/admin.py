from django.contrib import admin
from .models import student, subject, studentsPerSubject, sampleQuizzes, questions, reviewers

# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(studentsPerSubject)
admin.site.register(sampleQuizzes)
admin.site.register(questions)
admin.site.register(reviewers)
