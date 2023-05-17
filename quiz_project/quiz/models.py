from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
    QUESTION_STATUS = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    )

    question = models.CharField(max_length=255)
    options = models.JSONField()
    right_answer = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=QUESTION_STATUS, default='inactive')

    def update_status(self):
        now = timezone.now()
        if self.start_date <= now <= self.end_date:
            self.status = 'active'
        elif now > self.end_date:
            self.status = 'finished'
        self.save()

