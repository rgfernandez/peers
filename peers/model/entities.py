from elixir import *
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime

### Person objects

class Person(Entity):
    using_options(tablename="person", inheritance="multi")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    
    birthdate = Field(Date)
    first_name = Field(Unicode(30))
    middle_name = Field(Unicode(30))
    last_name = Field(Unicode(30))
    contact = Field(Unicode(30), unique=True, nullable=False)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)

def get_person_by_contact(k):
    """Get persons using contact number. Assume unique."""
    try:
        return Person.query.filter_by(contact=k).one()
    except NoResultFound:
        return None

def get_person_by_nick(n):
    return Person.query.filter_by(nick_name=n).all()

def get_person_by_name(ln='', fn='', mn=''):
    return Person.query.filter_by(first_name=fn,
                                middle_name=mn,
                                last_name=ln).all()

def set_contact(u, k):
    c = Person(created_by=u, modified_by=u)


class Person_Identifier(Entity):
    using_options(tablename="person_identifier")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    identifier = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)


class User(Entity):
    using_options(tablename="user")
    
    created = Field(DateTime, default=datetime.datetime.now)
    #created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    #modified_by = ManyToOne('User')
    voided = Field(DateTime)
    #voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    username = Field(Unicode(30), unique=True, nullable=False)
    password = Field(UnicodeText)
    role = ManyToOne('User_Role')
    health_center = Field(UnicodeText)
    
    OneToMany('Patient')
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)

def get_user_from_name(k):
    try:
        return User.query.filter_by(username=k).one()
    except NoResultFound:
        return None


class User_Role(Entity):
    using_options(tablename="user_role")
    
    created = Field(DateTime, default=datetime.datetime.now)
    #created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    #modified_by = ManyToOne('User')
    voided = Field(DateTime)
    #voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    name = Field(Unicode(30), nullable=False)
    description = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)


class Patient(Entity):
    using_options(tablename="patient")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    chits_id = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)

def create_patient(u, n, c):
    pass


### Location objects

class Location(Entity):
    using_options(tablename="location")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)


class Location_Name(Entity):
    using_options(tablename="location_name")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)


### Messaging objects

class Message(Entity):
    """Message object
    
    No one should be able to edit the message table (and related tables).
    Remember to commit! Methods defined here reference to an existing id.
    
    """
    # many types of messages
    using_options(tablename="msg", inheritance="multi")
    
    created = Field(DateTime, default=datetime.datetime.now)
            # incoming: on receive by server, outgoing: on create by server
    processed = Field(DateTime)
    sender = ManyToOne('Person')
    
    mode = Field(SmallInteger, default=3)
            # 0: unknown, 1: email, 2: sms, 3: http
    module = ManyToOne('Module')
    content = Field(UnicodeText, nullable=False)
    
    OneToMany('Message_Headers')
    OneToMany('Message_Attachments')
    OneToMany('Message_Notes')
    
    def set_header(self, header, value=None):
        """Add headers to current Message object"""
        if isinstance(header, basestring):
            if value is None:
                self.set_note('No value specified', 'error')
                return
            return Message_Headers(msg=self, header=header, value=value),
        
        contents = []
        for (elem, item) in header.items():
            contents.append(
                Message_Headers(msg=self, header=elem, value=item) )
        return tuple(contents)
    
    def set_attachment(self, name, type=None, content=None):
        """Add attachments to current Message object"""
        if isinstance(name, basestring):
            if type is None:
                self.set_note('No type specified', 'error')
                return
            if content is None:
                self.set_note('No content specified', 'error')
                return
            return Message_Headers(msg=self, name=name, type=type,
                                   content=content),
        
        contents = []
        for (elem, item) in header.items():
            contents.append(
                Message_Attachments(msg=self, name=elem,
                                    type=item[0], content=item[1]) )
        return tuple(contents)

    def set_note(self, note, type=0):
        """Add notes to current Message object"""
        if isinstance(type, basestring):
            if (type=='error'):
                type = 2
            elif (type=='warn'):
                type = 1
            else:   # info - default
                type = 0
        if isinstance(note, basestring):
            return Message_Notes(msg=self, type=type, note=note),
        
        contents = []
        for elem in note:
            contents.append(Message_Notes(msg=self, type=type, note=note))
        return contents
    
    def set_module(self, m):
        """Add module to current Message object"""
        self.set(module=m)

def get_mode(mode=None):
    if isinstance(mode, int):
        return mode         # already accepted value
    if not isinstance(mode, basestring):
        return 0            # unknown mode
    
    if (mode=='email'):
        return 1
    elif (mode=='sms'):
        return 2
    elif (mode=='http'):
        return 3
    else: # default
        return 0

def get_module(m):
    return Module.query.filter_by().all()


class Message_Headers(Entity):
    using_options(tablename="msg_headers")
    
    msg = ManyToOne('Message')
    header = Field(Unicode(30), nullable=False)
    value = Field(UnicodeText, nullable=False)


class Message_Attachments(Entity):
    using_options(tablename="msg_attachments")

    msg = ManyToOne('Message')
    name = Field(Unicode(30), nullable=False)
    type = Field(Unicode(30), nullable=False)
    content = Field(Binary, nullable=False)


class Message_Notes(Entity):
    using_options(tablename="msg_notes")
    
    msg = ManyToOne('Message')
    type = Field(SmallInteger, default=0, nullable=False)
            # 0: info, 1: warning, 2: error
    note = Field(UnicodeText)


class Message_Incoming(Message):
    using_options(tablename="msg_in", inheritance="multi")
    
    sender_created = Field(DateTime)


class Message_Outgoing(Message):
    using_options(tablename="msg_out", inheritance="multi")
    
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    OneToMany('Message_Outgoing_Receiver')
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)
    
def get_unsent(m=None):
    mode = get_mode(m)
    if m is None:
        return Message_Outgoing.query.filter_by(
                    voided=None, processed=None).all()
    return Message_Outgoing.query.filter_by(
                    voided=None, processed=None,
                    mode=m).all()


class Message_Outgoing_Receiver(Entity):
    using_options(tablename="msg_out_recv")
    
    msg = ManyToOne('Message_Outgoing')
    recv = ManyToOne('Person')


### Miscellaneous objects

class Module(Entity):
    using_options(tablename="module")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    module = Field(Unicode(30), nullable=False)
    description = Field(UnicodeText)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)


### Appointment objects

class Appointment(Entity):
    using_options(tablename="chits_apt")
    
    created = Field(DateTime, default=datetime.datetime.now)
    created_by = ManyToOne('User')
    modified = Field(DateTime, default=datetime.datetime.now)
    modified_by = ManyToOne('User')
    voided = Field(DateTime)
    voided_by = ManyToOne('User')
    void_reason = Field(UnicodeText)
    
    person = ManyToOne('Person')
    appointment = Field(Date)
    reminder_sent = Field(Boolean, default=0)
    
    def modify(self, u):
        self.set(modified_by=u, modified=datetime.datetime.now)
    
    def void(self, u, r):
        self.set(voided_by=u, voided=datetime.datetime.now,
                 void_reason=r)