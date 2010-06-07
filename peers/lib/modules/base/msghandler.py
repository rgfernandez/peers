# import modules inside the folder
from peers import model as m

__all__ = ['create_message',]

def parse_headers(h):
    if isinstance(h, dict):
        return h
    if not isinstance(h, basestring):
        return {}
    i = {}
    for elem in h.split('\n'):
        if not elem.strip():
            continue
        a,b,c = elem.partition(':')
        i[a.strip()] = c.strip()
    return i

def valid_contact(c):
    if not (c and isinstance(c, basestring)):
        return ''
    try:
        c = valid_phone(c)
    except:                 # only support phone numbers for now
        return ''
    return c

def valid_phone(c):
    c = c[1:] if c.startswith('+') else c
    if not c.isdigit():
        return ''
    # only support local numbers
    c = '63%s' % c[1:] if c.startswith('0') else c
    if len(c) != 12:       # not valid number
        return ''
    return c

def create_message(mode, **p):
    if 'name' in p:
        fn = p['name']
    else:
        fn = ''
    
    try:
        cn = p['contact']
        c = valid_contact(cn)
        if not c:
            return False
        contact = m.e.get_person_by_contact(c)
        if not contact:
            if fn:
                contact = m.e.Person(contact=c, first_name=fn)
            else:
                contact = m.e.Person(contact=c)
    except KeyError:
        return False
    
    try:
        text_content = p['body']
    except KeyError:
        return False
    
    try:
        headers = parse_headers(p['headers'])
    except KeyError:
        headers = {}
    
    try:
        attachments = p['attachments']
    except KeyError:
        attachments = {}
    
    # create incoming message
    msg = m.e.Message_Incoming(mode=m.e.get_mode(mode), sender=contact,
                               content=text_content)
    m.Session.commit()
    if headers:
        msg.set_header(headers)
    if attachments:
        msg.set_attachment(attachments)
    m.Session.commit()
    
    return True