from django.conf.urls.defaults import *
from parliament.models import Member

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from parliament import views

admin.autodiscover()

members_dict = { 'queryset': Member.objects.filter(left_reason="still_in_office").order_by("last_name"), }



urlpatterns = patterns('',
    # Example:
    #(r'^djangowfy/', include('django-twfy.parliament.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    (r'^members/$', 'django.views.generic.list_detail.object_list', members_dict),
    (r'^members/(?P<member_id>\d+)/$', 'parliament.views.memberdetail'),

)
