# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import oracledb

username = 'jykim@whatap.io'
password = 'Ahfmsek9413!'
database = 'ORCLPDB1'
hostname = 'localhost'  # Or the hostname of your Oracle Database
port = 1521  # Oracle Database port (default is 1521)

dsn = cx_Oracle.makedsn(hostname, port, database)
connection_string = f'oracle+cx_oracle://{username}:{password}@{dsn}'
engine = create_engine(connection_string, echo=True)  # Set echo to True for verbose output

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    nickname = Column(String(255))
class WhatapOracleAlchemy():
    def __init__(self, sql_config=None):

        self.sql_config = engine
        self.conn = None
        self.curs = None
        self.connect()

    def connect(self):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

        # Create tables if they do not exist
        Base.metadata.create_all(self.engine)
    def close(self):
        pass  # SQLAlchemy handles connection pooling and will automatically close connections

    def insert(self, email, nickname):
        # Create a new user record
        new_user = User(email=email, nickname=nickname)

        # Use a session to add the new user and commit the transaction
        session = self.Session()
        session.add(new_user)
        session.commit()
        session.close()

    def select_all(self):
        # Fetch and return all user records
        session = self.Session()
        records = session.query(User).all()
        session.close()
        return records

    def select_one(self, email):
        # Fetch and return a user record by email
        session = self.Session()
        record = session.query(User).filter_by(email=email).first()
        session.close()
        return record


if __name__ == "__main__":
    sql = WhatapOracleAlchemy()
    # Insert a new user
    sql.insert("jykim@test.com", "jykim")
    records = sql.select_all()
    for record in records:
        print(record)