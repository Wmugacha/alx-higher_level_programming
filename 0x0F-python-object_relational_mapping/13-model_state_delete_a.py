#!/usr/bin/python3
"""
script that lists State objects with the letter 'a' from
the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

if __name__ == "__main__":
    """
    Get the states from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)

    session.commit()

    session.close()
