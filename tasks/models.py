from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title