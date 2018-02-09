from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SurveyForm
from .models import SurveyResult


def index(request):
    return HttpResponse("Hello, world.")


def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            result = SurveyResult()
            result.name = form.cleaned_data['your_name']
            result.save()
            return HttpResponseRedirect('/')
    return render(request, 'survey.html')