from rest_framework import serializers
from .models import Meal, ExercisePlan, Symptom

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['description', 'photo_url']

class ExercisePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlan
        fields = ['name', 'description']

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['name', 'description']
