from rest_framework import generics, status
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer

# Create your views here.

class QuizList(generics.ListCreateAPIView):
    """
    API view to create the quiz by its ID.

    POST /quizzes/
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle POST request to create a quiz.

        Returns:
            Response: Response containing the created quiz.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ActiveQuiz(generics.ListAPIView):
    """
    API view to get the list of active quizzes.

    GET /quizzes/active/
    """
    queryset = Quiz.objects.filter(status='active')
    serializer_class = QuizSerializer

class QuizResult(generics.RetrieveAPIView):
    """
    API view to retrieve the result of a quiz by its ID.

    GET /quizzes/{id}/result/
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request to retrieve the result of a quiz.

        Returns:
            Response: Response containing the result of the quiz or 404 if the quiz doesn't exist or is not finished.
        """
        quiz = self.get_object()
        if quiz and quiz.status == 'finished':
            return Response({'rightAnswer': quiz.right_answer})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AllQuizzes(generics.ListAPIView):
    """
    API view to get the list of all quizzes.

    GET /quizzes/all/
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCachedView(APIView):
    @cache_page(60)  # Cache the response for 60 seconds
    def get(self, request, *args, **kwargs):
        # Handle GET request logic here
        return Response("OK")