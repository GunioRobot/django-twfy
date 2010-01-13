# coding=utf8

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.utils.translation import ugettext_lazy as _

CONFIRM_STATES = (
    (0,_('No')),
    (1,_('Yes')),
)

ENTER_REASONS = (
    ('unknown',_('Unknown')),
    ('general_election',_('General Election')),
    ('by_election',_('By-election')),
    ('changed_party',_('Changed party')),
    ('reinstated',_('Reinstated')),
    ('appointed',_('Appointed')),
    ('devolution',_('Devolution')),
    ('election',_('Election')),
    ('accession',_('Accession')),
    ('regional_election',_('Regional Election')),
    ('replaced_in_region',_('Replaced in Region')),
    ('became_presiding_officer',_('Became Presiding Officer')),    
)

LEFT_REASONS = (
    ('unknown',_('Unknown')),
    ('still_in_office',_('Still in Office')),
    ('general_election',_('General Election')),
    ('general_election_standing',_('General Election (standing)')),
    ('general_election_not_standing',_('General Election (not standing)')),
    ('changed_party',_('Changed party')),
    ('died',_('Died')),
    ('declared_void',_('Declared Void')),
    ('resigned',_('Resigned')),
    ('disqualified',_('Disqualified')),
    ('became_peer',_('Became Peer')),
    ('devolution',_('Devolution')),
    ('dissolution',_('Dissolution')),
    ('retired',_('Retired')),
    ('regional_election',_('Regional Election')),
    ('became_presiding_officer',_('Became Presiding Officer')),
)

PARTIES = (
    ('FF',_(u'Fianna Fáil')),
    ('FG',_(u'Fine Gael')),
    ('LAB',_(u'Labour Party')),
    ('GRN',_(u'Green Party')),
    ('SF',_(u'Sinn Féin')),
    ('PD',_(u'Progressive Democrats')),
    ('IND',_(u'Independent')),
    ('SOC',_(u'Socialist Party')),
    ('CC',_(u'Ceann Comhairle')),
    ('IND-FF',_(u'Independent Fianna Fáil')),
)

# Likewise each of these three lists belongs in Django metamodels but they're
# here because this is how the original DB works right now

HTYPES = (
    (10,_('Section title')),
    (11,_('Subsection title')),
    (12,_('Speech')),
    (13,_('Procedural text')),
)

MAJOR = (
    (1,_('Debates')),
    (3,_('Written Answers')),
    (7,_('Seanad Debates')),
)

MINOR = (
    (1,_('Question')),
    (2,_('Answer')),
)

class Chamber(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
	verbose_name = _("Chamber")
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=512)
    class Meta:
	verbose_name = _("Person")
	verbose_name_plural = _("People")
    def __unicode__(self):
        return self.name
    

class Expense(models.Model):
    year = models.DateField()
    person = models.ForeignKey(Person)
    salary = models.FloatField()
    allowance = models.FloatField()
    cta = models.FloatField()
    mea = models.FloatField()
    consphone = models.FloatField()
    officegrant = models.FloatField()
    office = models.FloatField()
    ssa = models.FloatField()
    mobile = models.FloatField()
    travel = models.FloatField()
    committeetravel = models.FloatField()
    isdn = models.FloatField()
    trainingtravel = models.FloatField()
    cttee_ent = models.FloatField()
    ipu = models.FloatField()
    bpa = models.FloatField()

class Alert(models.Model):
    alert_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=765)
    criteria = models.CharField(max_length=765)
    deleted = models.IntegerField()
    registrationtoken = models.CharField(max_length=102)
    confirmed = models.IntegerField(choices=CONFIRM_STATES)
    created = models.DateTimeField()
    class Meta:
        db_table = u'alerts'
	verbose_name = _("Email Alert")
    def __unicode__(self):
        return self.email + ":  " + self.criteria


class Twfyuser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=765)
    lastname = models.CharField(max_length=765)
    email = models.CharField(max_length=765)
    password = models.CharField(max_length=102)
    lastvisit = models.DateTimeField()
    registrationtime = models.DateTimeField()
    registrationip = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=39, blank=True)
    emailpublic = models.IntegerField(choices=CONFIRM_STATES)
    optin = models.IntegerField(choices=CONFIRM_STATES)
    deleted = models.IntegerField(choices=CONFIRM_STATES)
    postcode = models.CharField(max_length=30, blank=True)
    registrationtoken = models.CharField(max_length=72)
    confirmed = models.IntegerField(choices=CONFIRM_STATES)
    url = models.CharField(max_length=765,blank=True)
    api_key = models.CharField(unique=True, max_length=72, blank=True)
    class Meta:
        db_table = u'users'
	verbose_name = _("TWFY User")
    def __unicode__(self):
        return unicode(self.user_id) + " " + self.firstname + " " + self.lastname
	
class ApiKey(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Twfyuser,db_column='user_id')
    api_key = models.CharField(unique=True, max_length=72)
    commercial = models.IntegerField(choices=CONFIRM_STATES)
    created = models.DateTimeField()
    disabled = models.DateTimeField(null=True, blank=True)
    reason = models.TextField()
    class Meta:
        db_table = u'api_key'
    def __unicode__(self):
        return self.api_key

class Member(models.Model):
    id = models.IntegerField(primary_key=True,db_column='member_id')
    house = models.ForeignKey(Chamber,db_column='house')
    first_name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=765)
    constituency = models.CharField(max_length=300)
    party = models.CharField(choices=PARTIES,max_length=300)
    entered_house = models.DateField()
    left_house = models.DateField()
    entered_reason = models.CharField(max_length=72,choices=ENTER_REASONS)
    left_reason = models.CharField(max_length=87,choices=LEFT_REASONS)
    person_id = models.ForeignKey(Person, db_column='person_id')
    oir_personid = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=150, blank=True)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = u'member'
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Moffice(models.Model):
    moffice_id = models.AutoField(primary_key=True,db_column='moffice_id')
    dept = models.CharField(max_length=765,blank=True)
    position = models.CharField(max_length=600)
    from_date = models.DateField()
    to_date = models.DateField()
    person = models.ForeignKey(Person,db_column='person')
    source = models.CharField(max_length=765,blank=True)
    class Meta:
        db_table = u'moffice'
	verbose_name = _("Ministerial position")
        
class Hansard(models.Model):
    id = models.IntegerField(primary_key=True,db_column='epobject_id')
    gid = models.CharField(unique=True, max_length=255, blank=True)
    htype = models.IntegerField(choices=HTYPES)
    speaker_id = models.ForeignKey('Member',db_column='speaker_id')
    major = models.IntegerField(choices=MAJOR)
    section_id = models.IntegerField()
    subsection_id = models.IntegerField()
    hpos = models.IntegerField()
    hdate = models.DateField()
    htime = models.TimeField(blank=True)
    source_url = models.CharField(max_length=765)
    minor = models.IntegerField(null=True, blank=True, choices=MINOR)
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    colnum = models.IntegerField(null=True, blank=True)
    video_status = models.IntegerField()
    class Meta:
        db_table = u'hansard'
	verbose_name = _("Hansard object")
    def get_absolute_url(self):
        return "/debates/%i/" % self.id

    def __unicode__(self):
        return unicode(self.gid)

class Epobject(Hansard):
    epobject_id = models.OneToOneField('Hansard',db_column='epobject_id')
    raw_id_fields = ("epobject_id",)
    body = models.TextField(blank=True)
    type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'epobject'
    def __unicode__(self):
        return unicode(self.id)

class Anonvotes(models.Model):
    epobject_id = models.OneToOneField('Hansard',db_column='epobject_id',primary_key=True)
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()
    class Meta:
        db_table = u'anonvotes'
	verbose_name = _("Anonymous vote")
    def __unicode__(self):
        return unicode(self.epobject_id)

class Uservotes(models.Model):
    user_id = models.ForeignKey('Twfyuser',db_column='user_id')
    epobject_id = models.ForeignKey('Hansard',db_column="epobject_id")
    vote = models.IntegerField()
    class Meta:
        db_table = u'uservotes'
	verbose_name = _("User vote")
    def __unicode__(self):
        return unicode(self.epobject_id)

class Indexbatch(models.Model):
    indexbatch_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'indexbatch'
	verbose_name = _("Index batch")
	verbose_name_plural = _("Index batches")
    def __unicode__(self):
        return unicode(self.indexbatch_id)

class SearchQueryLog(models.Model):
    id = models.IntegerField(primary_key=True)
    query_string = models.TextField(blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    count_hits = models.IntegerField(null=True, blank=True)
    ip_address = models.TextField(blank=True)
    query_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'search_query_log'
	verbose_name = _("Search query")
	verbose_name_plural = _("Search queries")


"""
class Gidredirect(models.Model):
    gid_from = models.ForeignKey('Epobject',db_column="gid_from",unique=True)
    gid_to = models.ForeignKey('Epobject',db_column="gid_to",blank=True)
    hdate = models.DateField()
    major = models.IntegerField(choices=MAJOR)
    class Meta:
        db_table = u'gidredirect'


class Editqueue(models.Model):
    edit_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    edit_type = models.IntegerField(null=True, blank=True)
    epobject_id_l = models.IntegerField(null=True, blank=True)
    epobject_id_h = models.IntegerField(null=True, blank=True)
    glossary_id = models.IntegerField(null=True, blank=True)
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=765, blank=True)
    body = models.TextField(blank=True)
    submitted = models.DateTimeField(null=True, blank=True)
    editor_id = models.IntegerField(null=True, blank=True)
    approved = models.IntegerField(null=True, blank=True)
    decided = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'editqueue'

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    who = models.CharField(max_length=192)
    top = models.CharField(max_length=75)
    leftoffset = models.CharField(max_length=75)
    content = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'expenses'

class Glossary(models.Model):
    glossary_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765, blank=True)
    body = models.TextField(blank=True)
    wikipedia = models.CharField(max_length=765, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    visible = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'glossary'

class Memberinfo(models.Model):
    member_id = models.IntegerField()
    data_key = models.CharField(unique=True, max_length=300)
    data_value = models.TextField()
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = u'memberinfo'

class Mentions(models.Model):
    mention_id = models.IntegerField(primary_key=True)
    gid = models.CharField(unique=True, max_length=300, blank=True)
    type = models.IntegerField(unique=True)
    date = models.DateField(unique=True, null=True, blank=True)
    url = models.CharField(unique=True, max_length=765, blank=True)
    mentioned_gid = models.CharField(unique=True, max_length=300, blank=True)
    class Meta:
        db_table = u'mentions'

class PbcMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    member_id = models.IntegerField()
    chairman = models.IntegerField()
    bill_id = models.IntegerField()
    sitting = models.CharField(max_length=12)
    attending = models.IntegerField()
    class Meta:
        db_table = u'pbc_members'

class Personinfo(models.Model):
    person_id = models.IntegerField()
    data_key = models.CharField(unique=True, max_length=300)
    data_value = models.TextField()
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = u'personinfo'

class PostcodeLookup(models.Model):
    postcode = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=300)
    class Meta:
        db_table = u'postcode_lookup'

class Titles(models.Model):
    title = models.CharField(max_length=570, primary_key=True)
    class Meta:
        db_table = u'titles'

class Trackbacks(models.Model):
    trackback_id = models.IntegerField(primary_key=True)
    epobject_id = models.IntegerField(null=True, blank=True)
    blog_name = models.CharField(max_length=765, blank=True)
    title = models.CharField(max_length=765, blank=True)
    excerpt = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    posted = models.DateTimeField(null=True, blank=True)
    visible = models.IntegerField()
    source_ip = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'trackbacks'

class VideoTimestamps(models.Model):
    id = models.IntegerField(primary_key=True)
    gid = models.CharField(max_length=300)
    user_id = models.IntegerField(null=True, blank=True)
    atime = models.TextField() # This field type is a guess.
    deleted = models.IntegerField()
    whenstamped = models.DateTimeField()
    class Meta:
        db_table = u'video_timestamps'

"""
