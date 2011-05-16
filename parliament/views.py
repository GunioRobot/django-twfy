# Create your views here.

import settings
import hansardcalendar
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.db.models import Q
from parliament.models import Member, Hansard, Expense
from django.utils.safestring import mark_safe
from time import strftime, strptime
import sys
import re
import xapian



def index(request):
    return render_to_response('parliament/front.html',)

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

def expenses_xml(request,year):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/xml')

    exes_data = Expense.objects.filter(year=strftime("%Y-%m-%d",strptime(year,"%Y"))) # time.strptime(datestring,"%d%b%Y")

    t = loader.get_template('parliament/twfy_expenses_xml.txt')
    c = Context({
        'data': exes_data,
        'year': year,
    })
    response.write(t.render(c))
    return response

def search(request):
    searchdb = settings.XAPIAN_DB
    database = xapian.Database(searchdb)
    enquire = xapian.Enquire(database)
    if request.GET.get('s'):
        query_string = request.GET.get('s')
    else:
        query_string = ''

    response = HttpResponse(mimetype='text/html')

    qp = xapian.QueryParser()
    stemmer = xapian.Stem("english")
    qp.set_stemmer(stemmer)
    qp.set_database(database)
    qp.set_stemming_strategy(xapian.QueryParser.STEM_SOME)
    qp.set_default_op(xapian.Query.OP_AND)
    qp.add_boolean_prefix('speaker', 'S');
    qp.add_boolean_prefix('major', 'M');
    qp.add_boolean_prefix('date', 'D');
    qp.add_boolean_prefix('batch', 'B');
    qp.add_boolean_prefix('segment', 'U');
    qp.add_boolean_prefix('department', 'G');
    qp.add_boolean_prefix('party', 'P');
    qp.add_boolean_prefix('column', 'C');
    qp.add_boolean_prefix('gid', 'Q');

    query = qp.parse_query(query_string)
    
    enquire.set_query(query)
    matches = enquire.get_mset(0, 20)

    class Hit:
        pass
    
    resultset = []
    for m in matches:
        current = Hit()
        current.rank = m.rank + 1
        current.docid = m.docid
        current.path = m.document.get_data()
        current.percent = m.percent
        
        resultset.append(current)

    t = loader.get_template('parliament/search.html')
    c = Context ({
            'resultcount': matches.get_matches_estimated(),
            'results': resultset,
            
    })
    response.write(t.render(c))
    return response
