from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    accomplishmentDate = models.DateField()

    def __str__(self):
        return self.title
