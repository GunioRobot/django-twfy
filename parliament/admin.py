from django.contrib import admin
from parliament.models import Alert, Twfyuser, ApiKey, Member, Hansard, Epobject

class EpobjectInline(admin.TabularInline):
        model = Epobject
        exclude = ('htype','speaker_id','major','minor','section_id','subsection_id','hpos','hdate','htime','source_url','created','modified','colnum','video_status','type',)

class MemberAdmin(admin.ModelAdmin):
        list_display = ('__unicode__','party','constituency','entered_house','entered_reason','left_house')
        list_filter = ('house','left_reason')
        ordering = ('last_name',)

class AlertAdmin(admin.ModelAdmin):
        list_display = ('email','criteria','confirmed','created',)
        list_filter = ('confirmed',)
        ordering = ('email',)
        search_fields = ('email','criteria',)

class HansardAdmin(admin.ModelAdmin):
        inlines = [
                EpobjectInline,
        ]
        
admin.site.register(Alert,AlertAdmin)
admin.site.register(Twfyuser)
admin.site.register(ApiKey)
admin.site.register(Hansard,HansardAdmin)
admin.site.register(Member,MemberAdmin)


