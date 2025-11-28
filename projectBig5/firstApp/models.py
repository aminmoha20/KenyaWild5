from django.db import models

# Create your models here.
class homepage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    habitat = models.CharField(max_length=150, blank=True, null=True)
    average_weight_kg = models.FloatField(blank=True, null=True)
    lifespan_years = models.IntegerField(blank=True, null=True)
  