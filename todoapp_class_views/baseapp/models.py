from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField()
    status = models.IntegerField()
    created = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
