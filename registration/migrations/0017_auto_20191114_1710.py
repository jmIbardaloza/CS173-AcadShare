# Generated by Django 2.1.1 on 2019-11-14 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20191114_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choiceA',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choiceB',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choiceC',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='choiceD',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentspersubject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
