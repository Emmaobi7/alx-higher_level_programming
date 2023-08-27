#!/usr/bin/python3
"""print id of state searched"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).filter(State.name==sys.argv[4]).first()

    if states is None:
        print("Not found")
    else:
        print(states.id)

    session.close()
