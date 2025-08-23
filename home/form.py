from django import forms
from .models import Feedback

class FeedbackForm(forms.Modelform):
    class Meta:
        model = Feedback
        fields =['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder':'write your feedback...','row':4}),
        }