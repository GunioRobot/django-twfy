# Create your views here.

import settings
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from parliament.models import Member

def index(request):
    return HttpResponse("Hello, world. You're at django-twfy.parliament.views.index.")

    
def memberdetail(request, member_id):
    try:
        p = Member.objects.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404
    return render_to_response('parliament/member_detail.html', {'member': p},
        context_instance=RequestContext(request))


