#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

Session = sessionmaker()

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session.configure(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id):
        print(
            "{}: {}"
            .format(state.id, state.name)
        )
    session.close()
