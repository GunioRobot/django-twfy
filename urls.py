from django.conf.urls.defaults import *
from parliament.models import Member, Hansard

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from parliament import views

admin.autodiscover()


members_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office").order_by("last_name"), }
debates_dict = { 'queryset': Hansard.objects.filter(major=1,htype=10).order_by("hpos"), "date_field": "hdate",}
debates_month_dict = { 'queryset': Hansard.objects.filter(major=1,htype=10).order_by("hpos"), "date_field": "hdate","month_format":"%m", 'extra_context': {"dates":Hansard.objects.values('hdate').distinct()} }

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
    (r'^members/(?P<member_id>\d+)/$', 'parliament.views.memberdetail'),
    
    #  This one shows a debate index for Major type=1 at (eg) debates/2009/07/02
    (r'^debates/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', debates_month_dict),


    (r'^debates/(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', debates_month_dict),
    (r'^debates/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', debates_dict),
    (r'^debates/(?P<epobject_id>\d+)/$', 'parliament.views.hansarddetail'),
    
    (r'^expenses/expenses(?P<year>\d{4})\.xml$', 'parliament.views.expenses_xml'),
    
)
