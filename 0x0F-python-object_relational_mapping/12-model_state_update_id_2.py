#!/usr/bin/python3
''' script to change the name of a state.
'''

import sys
from model_state import Base, State
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
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
