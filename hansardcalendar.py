from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class HansardCalendar(HTMLCalendar):

    def __init__(self, hansards):
        super(HansardCalendar, self).__init__()
        self.hansards = self.group_by_day(hansards)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.hansards:
                cssclass += ' filled'
                body = ['<ul>']
                for hansard in self.hansards[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % hansard.get_absolute_url())
                    body.append(esc(hansard.title))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(HansardCalendar, self).formatmonth(year, month)

    def group_by_day(self, hansards):
        field = lambda hansard: hansards.hdate.day
        return dict(
            [(day, list(items)) for day, items in groupby(hansards, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

