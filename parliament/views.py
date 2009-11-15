# Create your views here.

import settings
import hansardcalendar
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from parliament.models import Member, Hansard
from django.utils.safestring import mark_safe


def index(request):
    return HttpResponse("Hello, world. You're at django-twfy.parliament.views.index.")

def memberdetail(request, member_id):
    try:
        p = Member.objects.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404
    return render_to_response('parliament/member_detail.html', {'member': p},
        context_instance=RequestContext(request))

def hansarddetail(request, epobject_id):
    try:
        parent = Hansard.objects.get(pk=epobject_id)
    except Hansard.DoesNotExist:
        raise Http404
    h = Hansard.objects.filter(Q(pk=epobject_id) | Q(section_id=epobject_id)).order_by("hpos")
    return render_to_response('parliament/hansard_detail.html', {'parent':parent, 'hansards': h, },
        context_instance=RequestContext(request))


