# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import MysqlConfig

# Connect to the database
# Define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255))
    nickname = Column(String(255))

class WhatapMySqlAlchemy():
    def __init__(self, sql_config=None):

        self.sql_config = sql_config if sql_config is not None else MysqlConfig()
        self.conn = None
        self.curs = None
        self.connect()

    def connect(self):
        self.engine = create_engine(f"mysql+pymysql://{self.sql_config.user}:{self.sql_config.password}@{self.sql_config.host}:{self.sql_config.port}/{self.sql_config.database}")
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
    sql = WhatapMySqlAlchemy()


    email = "ikorea@whatap.io"
    nickname = "fkorea"
    sql.insert(email=email, nickname=nickname)

    # Fetch and print all records
    records = sql.select_all()
    for record in records:
        print(f"ID: {record.id}, Email: {record.email}, Nickname: {record.nickname}")

    # Fetch and print a specific record
    email_to_find = "ikorea@whatap.io"
    record = sql.select_one(email_to_find)
    if record:
        print(f"Found record - ID: {record.id}, Email: {record.email}, Nickname: {record.nickname}")
    else:
        print(f"No record found for email: {email_to_find}")