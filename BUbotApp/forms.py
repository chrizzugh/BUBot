from django import forms
from BUbotApp.models import parallel_corpus 
from .models import *

class SaveReportForm(forms.ModelForm):
    class Meta:
        model = user_report
        fields = ["reportDescription" ,"reportAttachment"]

class SaveFeedbackForm(forms.ModelForm):
    class Meta:
        model = user_feedback
        fields = ["star" ,"feedbackDescription"]

class qaform(forms.ModelForm):
    class Meta:
        model = parallel_corpus
        fields = ["final_answer"]
