#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Conect to database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """
    Session objects provides all states
    """
    Session = sessionmaker(bind=engine)

    """ Create a Session object"""
    sess = Session()

    """ Show Query object """
    statess = sess.query(State).order_by(State.id).first()
    for i in statess:
        if ('a' in i.name):
            print(f"{i.id}: {i.name}")
    sess.close()
