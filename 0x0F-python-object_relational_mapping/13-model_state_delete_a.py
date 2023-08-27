#!/usr/bin/python3
"""deletes records with a in them"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    for state in session.query(State).order_by(State.id).filter(State.name.contains('a%')):
        session.delete(state)
    session.commit()
    session.close()
