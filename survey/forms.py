from django import forms


class SurveyForm(forms.Form):
    your_name = forms.CharField(label='Your name')