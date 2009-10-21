from django.contrib import admin
from parliament.models import Alert, Twfyuser, ApiKey, Member, Hansard

class MemberAdmin(admin.ModelAdmin):
        list_display = ('__unicode__','party','constituency','entered_house','entered_reason','left_house')
        list_filter = ('house','left_reason')
        ordering = ('last_name',)

class AlertAdmin(admin.ModelAdmin):
        list_display = ('email','criteria','confirmed','created',)
        list_filter = ('confirmed',)
        ordering = ('email',)
        search_fields = ('email','criteria',)
        
admin.site.register(Alert,AlertAdmin)
admin.site.register(Twfyuser)
admin.site.register(ApiKey)
admin.site.register(Hansard)
admin.site.register(Member,MemberAdmin)


