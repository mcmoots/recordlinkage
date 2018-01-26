from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index is also the match overview, because why not
def index(request):
    return HttpResponse("Hello world, this is the web app.")

# 
def review_match(request, match_id):
    # Process any POST input - display a confirmation message,
    # update the status of the previous match ID,
    # then display the highest-scoring unreviewed match

    return HttpResponse("This is the review page for RecordMatch %s.")
