#!/usr/bin/python3
'''
    script to fetch city by state.
'''

import sys

from model_state import Base, State
from model_city import City

from sqlalchemy.orm import sessionmaker,\
    relationship
from sqlalchemy import create_engine

if __name__ == '__main__':
    Session = sessionmaker()
    City.state = relationship("State", back_populates="cities")
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                               sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]
                           ),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    queries = session.query(State, City)\
        .filter(State.id == City.state_id).all()
    for state, city in queries:
        print("{}: ({}) {}".format(
            state.name,
            city.id,
            city.name
        ))
    session.close()
