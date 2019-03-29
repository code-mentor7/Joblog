from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Camdev(models.Model):
    JOB_LOG_PK = models.CharField(primary_key=True, max_length=100)
    IS_COMPLETE = models.CharField(max_length=10, null=True)
    SUBMIT_DT = models.DateTimeField()
    XPR_JOB_ID = models.CharField(max_length=100)
    OVRD_FILE_PATH = models.CharField(max_length=500)
    JOB_STATUS = models.CharField(max_length=10)
    API_JOB_NAME = models.CharField(max_length=100)
    X_RUN_ID = models.CharField(max_length=100, null=True)
    X_PROCESS_ID = models.CharField(max_length=100, null=True)
    X_LOG_PATH = models.CharField(max_length=500, null=True)
    X_SERVER = models.CharField(max_length=100, null=True)

    def __str__(self):
        """A string representation of the model."""
        return self.JOB_LOG_PK
