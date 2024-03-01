
from django.db import models

class UploadFile(models.Model):
    document = models.FileField(upload_to='uploads/')