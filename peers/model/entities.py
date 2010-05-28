from elixir import *

class Person(Entity):
    id = Field(Integer, primary_key=True)
    sex = Field(Unicode(1))
    birthdate = Field(DateTime)
