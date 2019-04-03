from django.db import models

class JOB_LOG(models.Model):
    JOB_LOG_PK = models.CharField(primary_key=True, max_length=50)
    IS_COMPLETE = models.CharField(max_length=50, null=True)
    SUBMIT_DT = models.DateTimeField(null=True)
    XPR_JOB_ID = models.CharField(max_length=50, null=True)
    OVRD_FILE_PATH = models.CharField(max_length=500, null=True)
    JOB_STATUS = models.CharField(max_length=50, null=True)
    API_JOB_NAME = models.CharField(max_length=50, null=True)
    X_RUN_ID = models.CharField(max_length=100, null=True)
    X_PROCESS_ID = models.CharField(max_length=50, null=True)
    X_LOG_PATH = models.CharField(max_length=200, null=True)
    X_SERVER = models.CharField(max_length=50, null=True)

    def __str__(self):
        """A string representation of the model."""
        return self.JOB_LOG_PK
