from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=200)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    start_date = models.DateField()
    stop_date = models.DateField()
    complete = models.BooleanField(default=False,  null=True, blank=True)

    def __str__(self):
        return self.task