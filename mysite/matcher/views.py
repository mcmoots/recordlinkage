from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from matcher.models import PatientRecord, RecordMatch

# Create your views here.

# index is also the match overview, because why not
def index(request):

    match_list = RecordMatch.objects.order_by('-score')
    template = loader.get_template('matcher/index.html')
    context = {
            'match_list': match_list,
            }
    return HttpResponse(template.render(context, request))

# 
def review_match(request, match_id):
    # Process any POST input - display a confirmation message,
    # update the status of the previous match ID,
    # then display the highest-scoring unreviewed match


    return HttpResponse("This is the review page for RecordMatch %s." % match_id)
