#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MealSerializer, ExercisePlanSerializer, SymptomSerializer
from rest_framework.decorators import action

class AnalyzeMeal(APIView):
    def get(self, request):
        # Vous pouvez par exemple renvoyer un message de bienvenue ou des infos
        return Response({"message": "Please send a POST request to analyze a meal."})

    def post(self, request):
        meal_description = request.data.get('meal_description')
        meal_photo = request.data.get('meal_photo')
        # Logique d'analyse du repas
        analysis = {"calories": 500, "protein": 30, "fat": 10, "carbs": 60}
        return Response({"analysis": analysis})

class RecommendExercise(APIView):
    def post(self, request):
        user_profile = request.data.get('user_profile')
        # Logique de recommandation d'exercices
        exercise_plan = [{"exercise": "Squats", "sets": 3, "reps": 12}]
        return Response({"exercise_plan": exercise_plan})

class DiagnoseSymptoms(APIView):
    def post(self, request):
        symptoms = request.data.get('symptoms')
        # Logique de diagnostic des symptômes
        advice = "You may have a common cold. Rest and hydrate."
        return Response({"advice": advice})

