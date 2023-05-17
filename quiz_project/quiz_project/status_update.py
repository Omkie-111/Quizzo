import os
from datetime import datetime
from crontab import CronTab
from pymongo import MongoClient
from django.conf import settings
from quiz.models import Quiz

def update_quiz_statuses():
    current_time = datetime.now()
    quizzes = Quiz.objects.all()
    for quiz in quizzes:
        if quiz.start_date <= current_time <= quiz.end_date:
            quiz.status = 'active'
        elif current_time > quiz.end_date:
            quiz.status = 'finished'
        else:
            quiz.status = 'inactive'
        quiz.save()


def create_cron_job():
    script_path = os.path.join(os.getcwd(), 'status_update.py')
    cron = CronTab(user=True)
    job = cron.new(command=f'python3 {script_path}')
    job.minute.every(1)  # Runs every minute, adjust as needed
    cron.write()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
    client = MongoClient(settings.DATABASES['default']['HOST'])
    db = client[settings.DATABASES['default']['NAME']]
    update_quiz_statuses()
    create_cron_job()
