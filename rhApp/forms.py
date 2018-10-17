from django import forms
from .models import QuestionM, ChoiceM

class rhSurvey(forms.Form):
    answers_radio = forms.CharField(widget=forms.RadioSelect, choices=[])

    def __init__(self, arg):
