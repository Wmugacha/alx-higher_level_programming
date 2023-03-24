#!/usr/bin/python3
"""
script that lists State objects from
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

    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print('Nothing')
    else:
        print("{0}: {1}".format(instance.id, instance.name))
