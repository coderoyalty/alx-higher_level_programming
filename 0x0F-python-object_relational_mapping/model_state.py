#!/usr/bin/python3
'''
    class definition of a State.
'''

import MySQLdb
from sqlalchemy import Column, Integer, String
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
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
