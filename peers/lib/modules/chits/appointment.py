from peers import model as m
import datetime
import re

__all__ = []

def add_appointment(u, p, d):
    if isinstance(d, basestring):
        a = [int(e) for e in '\n'.join(re.findall('\d*', d)).split()]
        if len(a) == 2:
            curr_time = datetime.datetime.now()
            if a > [curr_time.month, curr_time.date]:
                a.insert(0, curr_time.year)     # appointment in current year
            else:
                a.insert(0, curr_time.year+1)   # appointment for next year
        if len(a) < 3:
            return None
        d = datetime.datetime(*a)
    if not isinstance(d, list):     # datetime superclass
        return None
    apt = m.e.Appointment(created_by=u, modified_by=u, person=p,
                          appointment=d)