from django import template
from datetime import date, datetime, timedelta
import pytz

register = template.Library()

#Days Output as difference between input datetime and now 
@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - datetime.utcnow().replace(tzinfo=pytz.utc)

    if delta.days == 0:
        return "Today"
    elif delta.days < 1:
        return "%s %s ago" % (abs(delta.days),
            ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days


from ..models import T_Memory_Palace_Type

#Filtering on foreign key
@register.filter(name='get_dictionary_value_from_variable2')
def get_dictionary_value_from_variable2(key):
    t = T_Memory_Palace_Type.objects.filter(id=key)
    return t
