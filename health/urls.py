from django.urls import path
from .views import AnalyzeMeal, RecommendExercise, DiagnoseSymptoms

urlpatterns = [
    path('nutrition/analyze/', AnalyzeMeal.as_view(), name='analyze_meal'),
    path('exercise/recommend/', RecommendExercise.as_view(), name='recommend_exercise'),
    path('symptoms/diagnose/', DiagnoseSymptoms.as_view(), name='diagnose_symptoms'),
]
