#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco" from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add objects to the session and commit changes
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Close session
    session.close()
