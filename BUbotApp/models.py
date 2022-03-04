from django.db import models

# Create your models here.

class user_report (models.Model):
    reportDescription =  models.TextField()
    reportAttachment = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

class user_feedback(models.Model):
    star = models.IntegerField() 
    feedbackDescription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class bubotcollection (models.Model):
    model = models.FileField(blank=True)
    vocabulary = models.FileField(blank=True)
    abbreviations = models.FileField(blank=True)
    embedded = models.FileField(blank=True)