from django.contrib import admin
from parliament.models import Alert, Twfyuser, ApiKey, Member, Hansard, Moffice, Epobject, Anonvotes, Indexbatch, Uservotes, SearchQueryLog, Chamber, Person, Expense

class EpobjectInline(admin.TabularInline):
        model = Epobject
        exclude = ('htype','speaker_id','major','minor','section_id','subsection_id','hpos','hdate','htime','source_url','created','modified','colnum','video_status','type',)

class AnonvotesInline(admin.TabularInline):
	model = Anonvotes

class MofficeInline(admin.TabularInline):
        model = Moffice
        
class ExpenseInline(admin.TabularInline):
        model = Expense

class MemberAdmin(admin.ModelAdmin):
        list_display = ('__unicode__','party','constituency','entered_house','entered_reason','left_house')
        list_filter = ('house','left_reason')
        ordering = ('last_name',)

class PersonAdmin(admin.ModelAdmin):
        ordering = ('name',)
        inlines = [
                MofficeInline,
                ExpenseInline,
        ]

class AlertAdmin(admin.ModelAdmin):
        list_display = ('email','criteria','confirmed','created',)
        list_filter = ('confirmed',)
        ordering = ('email',)
        search_fields = ('email','criteria',)

class HansardAdmin(admin.ModelAdmin):
        inlines = [
                EpobjectInline,AnonvotesInline
        ]

class IndexbatchAdmin(admin.ModelAdmin):
	list_display = ('indexbatch_id','created',)
	
class SearchQueryLogAdmin(admin.ModelAdmin):
        list_display = ('query_time','query_string','count_hits',)
        ordering = ('-query_time',)
	list_filter = ('count_hits',)

admin.site.register(Alert,AlertAdmin)
admin.site.register(Twfyuser)
admin.site.register(ApiKey)
admin.site.register(Indexbatch,IndexbatchAdmin)
admin.site.register(Hansard,HansardAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(SearchQueryLog,SearchQueryLogAdmin)
admin.site.register(Chamber)
admin.site.register(Person,PersonAdmin)

