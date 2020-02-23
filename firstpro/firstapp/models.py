from django.db import models

class modeltable(models.Model):
    name=models.CharField(max_length=264)
    ingredients=models.CharField(max_length=264)
    time=models.CharField(max_length=264)
    directions=models.CharField(max_length=264)
    description=models.CharField(max_length=264)
    image=models.FileField(upload_to='fileupload')
