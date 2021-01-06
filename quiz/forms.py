from django import forms
from django.forms import fields
from .models import QuizTitle, Question

class TitleForm(forms.ModelForm):
    class Meta:
        model = QuizTitle
        fields = ['title']
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['title']