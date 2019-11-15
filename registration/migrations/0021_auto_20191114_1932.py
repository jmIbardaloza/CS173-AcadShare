# Generated by Django 2.1.1 on 2019-11-14 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20191114_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='questionNumber',
        ),
        migrations.AlterField(
            model_name='studentspersubject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
