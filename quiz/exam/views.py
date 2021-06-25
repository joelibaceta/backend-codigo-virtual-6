from exam.serializers import QuestionSerializer
from exam.serializers import OptionSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from exam.models import Question, Option, Answer


# Create your views here.
class QuestionsAPI(APIView):

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class OptionsAPI(APIView):

    def get(self, request, pk):
        questions = Option.objects.filter(question_id = pk)
        serializer = OptionSerializer(questions, many=True)
        return Response(serializer.data)

class AnswersAPI(APIView):

    def post(self, request):
        data = request.data
        #request.files 
        answers = Answer()

        answers.create(data)
        return Response("OK")