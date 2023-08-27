#!/usr/bin/python3
"""changes name of record in table"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    for state in session.query(State).order_by(State.id).filter(State.id == 2):
        state.name = "New Mexico"
    session.commit()
    session.close()
