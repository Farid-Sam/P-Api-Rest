#from django.db import models

# Create your models here.
from django.db import models

class Meal(models.Model):
    description = models.TextField()
    photo_url = models.URLField()

    def __str__(self):
        return self.description

class ExercisePlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

