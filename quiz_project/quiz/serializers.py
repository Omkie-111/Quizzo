from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    """
        Create API serialiser for the app
    """
    class Meta:
        model = Quiz
        fields = '__all__'