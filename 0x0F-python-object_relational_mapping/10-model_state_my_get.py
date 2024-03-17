#!/usr/bin/python3
"""Script that prints the State object with the given name from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print state id or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
