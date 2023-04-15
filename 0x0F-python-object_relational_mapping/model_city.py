#!/usr/bin/python3
'''class definition of a City.
'''

from model_state import Base
from sqlalchemy import Column, Integer,\
    String,\
    ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    '''The class links to the MySQL table `cities`.
    class attribute:
        id represents a column of unique,
        auto-generated integer that can't be null
        and is a primary key.
        name represents a column of max. 128 characters
        that can't be null.
        state_id represents a column of an integer, that
        can't be null and is a foreign key to `State.id`.
    '''
    __tablename__ = "cities"
    id = Column(Integer, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)
