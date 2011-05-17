
Q:  Huh?

A:  TheyWorkForYou.com is open source, and both Ireland and Australia have 
    copies running. However, it uses an 18th-century character set, in no way 
    separates content from design and the current version of PHP (5.3) won't 
    run it at all without generating fatal errors. Which is really PHP's fault
    for changing almost all its error handling rules.
    
Q:  So...

A:  So I'm rewriting the part of it that causes the concerns above.

Q:  Which is?

A:  The DB schema in this one is reset to UTF-8, and we're dumping the entire 
    web-facing PHP app in favour of a Django (http://djangoproject.org) 
    application.  You can use the Django admin already because the entire DB 
    (well, the bits used in Ireland anyway) has been described as Django models.
    
    Django is also templated.  And it more or less requires Unicode, which 
    suits us for a large number of reasons, including future support for >1 
    languages.
    
    And it supports i18n. Support for which is slightly sketchy here at the 
    moment but do please step in and mark strings I 
    
Q:  I want to make a version of TheyWorkForYou.com which works in my country

A:  Then install it, then install this and use it for the web-facing side.

Q:  What won't it do?

A:  Nothing in TWFY's scripts/ or search/ directories are being ported. That's
    because we don't need to!  That's the joy of keeping their schema - all the
    lovely email alert mailers, Xapian-backed search stuff, or command-line
    tools should work just fine without modification (* this is a lie. There's
    a couple of charset issues you'll need to tweak. I'll detail them when the
    actual web app is done.)
    
Q:  "When the actual web app is done" ??

A:  Yeah. It's not finished yet.  It still needs:

        * To provide all the search query stuff in a way that's backwards-
          compatible.  That's now progressing at a clip. You'll need xapian.py
          
        * Several views which aren't finished yet
        
        * Django-registration and user profile support to handle annotations
          and email alert records
          
        * The aforementioned i18n strings to be set
        
        * A design that unsucks.  I'm working on it alongside @SabrinaDent, who
          has the misfortune of having married me.
          
        * A fixtures file.  We're considering "The Importance of Being Earnest",
          because it's a play, and it's from Ireland.  Plays are good because
          they have characters (members of Parliament) who say things (speeches)
          in discrete scenes (debates) which are surrounded by stage directions
          (procedural text).
          
        * Probably other things.  We (kildarestreet.com) really need this thing
          to get finished and it's back on the boil, so to speak, so assume that
          we'll have a feature-complete Django clone of TWFY up and running 
          fairly soon now.  Later we'll discuss forking it into something that
          uses Haystack instead for search, but then you're pretty much on your
          own with email alerts, sadly.
          
--- John Handelaar, 2011-05-17 
        
