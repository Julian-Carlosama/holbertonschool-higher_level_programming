#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ Conect to database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """
    Session object provides the entrypoint to acquire a Query object
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    query() takes one or more entities and returns a
    new Query object which will issue mapper queries within
    the context of this Session
    """
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
