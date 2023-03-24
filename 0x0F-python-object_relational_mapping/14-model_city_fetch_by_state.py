#!/usr/bin/python3
"""
script that prints all City objects from
the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

if __name__ == "__main__":
    """
    Get the cities from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(City, State).join(State).all():
        print("{}: ({:d}) {}".format(instance.State.name,
                                     instance.City.id, instance.City.name))
