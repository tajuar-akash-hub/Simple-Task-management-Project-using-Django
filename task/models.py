from django.db import models
from category.models import catagory_model


# Create your models here.
class task_model(models.Model):
    task_title = models.CharField( max_length=50)
    task_description = models.TextField()
    task_catagory = models.ManyToManyField(catagory_model)
    is_completed = models.BooleanField(default = False)
    task_assign_date= models.DateField()

    def __str__(self) -> str:
        return f'Task name = {self.task_title}'
    