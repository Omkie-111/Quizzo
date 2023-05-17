from django.urls import path
from .views import QuizList, ActiveQuiz, QuizResult, AllQuizzes

urlpatterns = [
    path('quizzes/', QuizList.as_view(), name='quiz-list'),
    path('quizzes/active/', ActiveQuiz.as_view(), name='active-quiz'),
    path('quizzes/<int:pk>/result/', QuizResult.as_view(), name='quiz-result'),
    path('quizzes/all/', AllQuizzes.as_view(), name='all-quizzes'),
]
