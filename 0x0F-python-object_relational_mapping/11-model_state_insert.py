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
    Insert a new State object to database
    """
    new_St = State(name='Louisiana')
    session.add(new_St)
    session.commit()

    print(new_St.id)
