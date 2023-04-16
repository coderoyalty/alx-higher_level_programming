#!/usr/bin/python3
''' script to insert a new state
'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Session = sessionmaker()

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                               sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]
                           ))
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()
