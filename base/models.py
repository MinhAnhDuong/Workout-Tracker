from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'

class TrainingRecord(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='records_group')
    date = models.DateField()
    series = models.CharField(max_length=50, null=True, blank=True)
    repetitions = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ["-date"]