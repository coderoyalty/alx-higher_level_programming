#!/usr/bin/python3

'''
    class definition of a State.
'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        This class links to mysql table called states
        it inherits from Base.
        class attribute:
        id represents a column a unique, auto-incremented,
        integer which is the primary key of the table.
        name represent a column with a maximum of 128 characters,
        not nullable string.
    """
    __tablename__ = "states"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True,
                           nullable=False
                           )
    name = sqlalchemy.Column(sqlalchemy.String(128),
                             nullable=False)
