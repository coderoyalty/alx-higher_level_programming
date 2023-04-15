#!/usr/bin/python3
''' script to delete a state.
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
    session.query(State).filter(State.name.like("%a%"))\
        .delete(synchronize_session='fetch')
    session.commit()
    session.close()
