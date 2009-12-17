# Template tag
from datetime import date, timedelta, datetime
from django import template
from django.contrib.contenttypes.models import ContentType
from parliament.models import Expense
register = template.Library()


def expenses(personid):
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT salary,travel,mobile,mea,office,officegrant,consphone,cta,isdn,allowance,ssa,committeetravel,cttee_ent,bpa,ipu,salary+travel+mobile+mea+office+officegrant+consphone+cta+isdn+allowance+ssa+committeetravel+cttee_ent+bpa+ipu FROM parliament_expense WHERE person_id = %s ORDER BY year ASC", [personid])

    rows = cursor.fetchall()
    rows += (("Salary","Travel & Subsistence Allowance","Mobile phone","Misc. Expenses","Constituency Office","Constituency Office Grant","Constituency Phone","Constituency Travel Allowance","ISDN Line Rental","Ex-Officio Allowances","Special Secretarial Allowance","Committee Travel Expenses","Committee Entertainment Expenses","British-Irish Parliamentary Association","Inter-Parliamentary Union","Total",),)
    rotated = zip(*rows[::-1])

    return {'expenses': rotated,}

register.inclusion_tag('parliament/expense.html')(expenses)

