from django import forms
  
# import feedback_report from models.py
from .models import *

class SaveReportForm(forms.ModelForm):
    class Meta:
        model = user_report
        fields = ["reportDescription" ,"reportAttachment"]

class SaveFeedbackForm(forms.ModelForm):
    class Meta:
        model = user_feedback
        fields = ["star" ,"feedbackDescription"]
        # exclude = ["reportDescription" ,"reportAttachment"]



