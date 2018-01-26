from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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
    confirmation_message = ''

    try:
        prev_match = get_object_or_404(RecordMatch, id=request.POST['match_id'])
    except KeyError:
        pass
    except Http404:
        error_message = "Whoa you tried to review a match that doesn't exist"
    else:
        if request.POST['determination']=='accept':
            prev_match.review_state='ACCEPTED'
            confirmation_message='Match was marked as valid.'
        elif request.POST['determination']=='reject':
            prev_match.review_state='REJECTED'
            confirmation_message='Match was marked as not valid.'
        elif request.POST['determination']=='skip':
            prev_match.review_state='UNREVIEWED'
            confirmation_message='Match was marked as to-do.'
        else:
            prev_match.review_state='UNREVIEWED'
            confirmation_message='Wow that was weird. Match was marked as unreviewed just to be safe.'
        prev_match.save()
        new_match = RecordMatch.objects.filter(review_state__exact='UNREVIEWED').order_by('-score').first()

        return render(request, 'matcher/match_review.html',
                {'match' : get_object_or_404(RecordMatch, id=new_match.id),
                    'confirmation_message' : confirmation_message,
                    })

    # No POST data



    return render(request, 'matcher/match_review.html', 
           {'match' : get_object_or_404(RecordMatch, id=match_id),
            'confirmation_message' : confirmation_message,
            })
