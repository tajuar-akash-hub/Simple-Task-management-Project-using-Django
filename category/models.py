from django.db import models


# Create your models here.
class catagory_model(models.Model):
    catagory_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.catagory_name}'
    # models.ManyToManyField("task_model")
#     TaskCategory Model will have
# Category Name
# Many-to-Many Relationships with task model        
