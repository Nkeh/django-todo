from django.db import models

# Create your models here.

class Task(models.Model):
    """Model definition for Todo."""

    # TODO: Define fields here
    title = models.CharField(max_length=200, null=False, blank= False)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField()
    

    class Meta:
        pass

    def __str__(self):
        return self.title
