# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

CONFIRM_STATES = (
    (0,'No'),
    (1,'Yes'),
)

HOUSES_OF_PARLIAMENT = (
    (1,'Dail'),
    (4,'Seanad'),
)

ENTER_REASONS = (
    ('unknown','Unknown'),
    ('general_election','General Election'),
    ('by_election','By-election'),
    ('changed_party','Changed party'),
    ('reinstated','Reinstated'),
    ('appointed','Appointed'),
    ('devolution','Devolution'),
    ('election','Election'),
    ('accession','Accession'),
    ('regional_election','Regional Election'),
    ('replaced_in_region','Replaced in Region'),
    ('became_presiding_officer','Became Presiding Officer'),    
)

LEFT_REASONS = (
    ('unknown','Unknown'),
    ('still_in_office','Still in Office'),
    ('general_election','General Election'),
    ('general_election_standing','General Election (standing)'),
    ('general_election_not_standing','General Election (not standing)'),
    ('changed_party','Changed party'),
    ('died','Died'),
    ('declared_void','Declared Void'),
    ('resigned','Resigned'),
    ('disqualified','Disqualified'),
    ('became_peer','Became Peer'),
    ('devolution','Devolution'),
    ('dissolution','Dissolution'),
    ('retired','Retired'),
    ('regional_election','Regional Election'),
    ('became_presiding_officer','Became Presiding Officer'),
)

HTYPES = (
    (10,'Section title'),
    (11,'Subsection title'),
    (12,'Speech'),
    (13,'Procedural'),
)

MAJOR = (
    (1,'Debates'),
    (3,'Written Answers'),
    (7,'Seanad Debates'),
)

MINOR = (
    (1,'Question'),
    (2,'Answer'),
)

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
	verbose_name = "Email Alert"
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
	verbose_name = "TWFY User"
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
    house = models.IntegerField(choices=HOUSES_OF_PARLIAMENT)
    first_name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=765)
    constituency = models.CharField(max_length=300)
    party = models.CharField(max_length=300)
    entered_house = models.DateField()
    left_house = models.DateField()
    entered_reason = models.CharField(max_length=72,choices=ENTER_REASONS)
    left_reason = models.CharField(max_length=87,choices=LEFT_REASONS)
    person_id = models.IntegerField()
    oir_personid = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=150, blank=True)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = u'member'
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


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
	verbose_name = "Hansard object"

    def __unicode__(self):
        return unicode(self.gid)


class Epobject(Hansard):
    epobject_id = models.OneToOneField('Hansard',db_column='epobject_id',primary_key=True)
    raw_id_fields = ("epobject_id",)
    body = models.TextField(blank=True)
    type = models.IntegerField(null=True, blank=True)
    #created = models.DateTimeField(null=True, blank=True)
    #modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'epobject'
    def __unicode__(self):
        return unicode(self.id)
"""

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


class Anonvotes(models.Model):
    epobject_id = models.IntegerField(primary_key=True)
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()
    class Meta:
        db_table = u'anonvotes'

class Expenses(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    who = models.CharField(max_length=192)
    top = models.CharField(max_length=75)
    leftoffset = models.CharField(max_length=75)
    content = models.CharField(max_length=768, blank=True)
    class Meta:
        db_table = u'expenses'

class Gidredirect(models.Model):
    gid_from = models.CharField(unique=True, max_length=180, blank=True)
    gid_to = models.CharField(max_length=180, blank=True)
    hdate = models.DateField()
    major = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'gidredirect'

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

class Indexbatch(models.Model):
    indexbatch_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'indexbatch'

class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    house = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(unique=True, max_length=300, blank=True)
    last_name = models.CharField(unique=True, max_length=765)
    constituency = models.CharField(max_length=300)
    party = models.CharField(max_length=300)
    entered_house = models.DateField(unique=True)
    left_house = models.DateField()
    entered_reason = models.CharField(max_length=72)
    left_reason = models.CharField(max_length=87)
    person_id = models.IntegerField()
    oir_personid = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=150)
    lastupdate = models.DateTimeField()
    class Meta:
        db_table = u'member'

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

class Moffice(models.Model):
    moffice_id = models.IntegerField(primary_key=True)
    dept = models.CharField(max_length=765)
    position = models.CharField(max_length=600)
    from_date = models.DateField()
    to_date = models.DateField()
    person = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=765)
    class Meta:
        db_table = u'moffice'

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

class SearchQueryLog(models.Model):
    id = models.IntegerField(primary_key=True)
    query_string = models.TextField(blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    count_hits = models.IntegerField(null=True, blank=True)
    ip_address = models.TextField(blank=True)
    query_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'search_query_log'

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

class Uservotes(models.Model):
    user_id = models.IntegerField()
    epobject_id = models.IntegerField()
    vote = models.IntegerField()
    class Meta:
        db_table = u'uservotes'

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
