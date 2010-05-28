"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from peers.model import meta

import elixir
from peers.model.entities import *

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    #meta.Session.configure(bind=engine)
    #meta.engine = engine
    elixir.session.configure(bind=engine)
    metadata.bind = engine

Session = elixir.session = meta.Session
metadata = elixir.metadata
elixir.options_defaults.update({
    'autoload': True,
})

if ( elixir.options_defaults.get('autoload', False)
     and not metadata.is_bound() ):
    elixir.delay_setup = True

if not elixir.options_defaults.get('autoload', False):
    elixir.setup_all(True)


## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
