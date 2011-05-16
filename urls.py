# coding=utf8
from django.conf.urls.defaults import *
from parliament.models import Member, Hansard
from parliament import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

nohouse_context = {'house_name':'Houses of the Oireachtas', }
dail_context = {'house':1,'path':'debates','title':'Dáil Debates','house_name':'Dáil Éireann',}
seanad_context = {'house':7,'path':'seanad','title':'Seanad Debates','house_name':'Seanad Éireann',}
wrans_context = {'house':3,'path':'wrans','title':'Written Answers','house_name':'Dáil Éireann',}

members_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office").order_by("last_name"), 'extra_context':nohouse_context,}
tds_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office",house=1).order_by("last_name"), 'extra_context':dail_context,}
senators_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office",house=4).order_by("last_name"), 'extra_context':seanad_context,}

debates_dict = { 'queryset': Hansard.objects.filter(major=1,htype=10).order_by("hpos"), "date_field": "hdate", 'extra_context':dail_context,}
debates_month_dict = { 'queryset': Hansard.objects.filter(major=1,htype=10).order_by("hpos"), "date_field": "hdate","month_format":"%m", 'extra_context': {"dates":Hansard.objects.values('hdate').distinct(),"context":dail_context,} }

sendebates_dict = { 'queryset': Hansard.objects.filter(major=7,htype=10).order_by("hpos"), "date_field": "hdate",  'extra_context':seanad_context,}
sendebates_month_dict = { 'queryset': Hansard.objects.filter(major=7,htype=10).order_by("hpos"), "date_field": "hdate","month_format":"%m", 'extra_context': {"dates":Hansard.objects.values('hdate').distinct(),"context":seanad_context,} }

wrans_dict = { 'queryset': Hansard.objects.filter(major=3,htype=10).order_by("hpos"), "date_field": "hdate", 'extra_context':wrans_context,}
wrans_month_dict = { 'queryset': Hansard.objects.filter(major=3,htype=10).order_by("hpos"), "date_field": "hdate","month_format":"%m", 'extra_context': {"dates":Hansard.objects.values('hdate').distinct(),"context":wrans_context,} }


urlpatterns = patterns('',
    # Example:
    #(r'^djangowfy/', include('django-twfy.parliament.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'parliament.views.index'),
    (r'^members/$', 'django.views.generic.list_detail.object_list', members_dict),
    (r'^tds/$', 'django.views.generic.list_detail.object_list', tds_dict),
    (r'^senators/$', 'django.views.generic.list_detail.object_list', senators_dict),
    (r'^members/(?P<member_id>\d+)/$', 'parliament.views.memberdetail'),
    
    #  This one shows a debate index for Major type=1 at (eg) debates/2009/07/02
    (r'^debates/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', debates_month_dict),
    (r'^debates/(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', debates_month_dict),
    (r'^debates/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', debates_dict),
    (r'^debates/(?P<epobject_id>\d+)/$', 'parliament.views.hansarddetail'),
    
    (r'^seanad/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', sendebates_month_dict),
    (r'^seanad/(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', sendebates_month_dict),
    (r'^seanad/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', sendebates_dict),
    (r'^seanad/(?P<epobject_id>\d+)/$', 'parliament.views.hansarddetail'),

    (r'^wrans/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', wrans_month_dict),
    (r'^wrans/(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', wrans_month_dict),
    (r'^wrans/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', wrans_dict),
    (r'^wrans/(?P<epobject_id>\d+)/$', 'parliament.views.hansarddetail'),

    (r'^expenses/expenses(?P<year>\d{4})\.xml$', 'parliament.views.expenses_xml'),

    (r'^search/$','parliament.views.search'),

)
