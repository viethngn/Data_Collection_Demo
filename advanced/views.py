from django.http import HttpResponse
from django.shortcuts import render
from survey.models import SurveyResult


def view_names(request):
    return render(request, 'view_names.html', {
        'names': [r.name for r in SurveyResult.objects.all()]
    })
