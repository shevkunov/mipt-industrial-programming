from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True)
    was_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
