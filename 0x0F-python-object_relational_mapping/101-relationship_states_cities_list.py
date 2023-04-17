#!/usr/bin/python3
'''
script to list relationship (between State and City)
'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(
                               sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]
                           ),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    queries = session.query(State).order_by(State.id).all()

    for state in queries:
        cities = state.cities
        print(
            "{}: {}"
            .format(state.id, state.name)
        )
        for city in cities:
            print(
                "\t{}: {}"
                .format(city.id, city.name)
            )
    session.close()
