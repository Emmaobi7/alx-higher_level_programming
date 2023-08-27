#!/usr/bin/python3
"""outputs first state in db"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == '__main__':
    engine = engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if (state is None):
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
