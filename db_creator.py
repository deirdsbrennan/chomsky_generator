# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:08:12 2020

@author: Owner
"""

# db_creator.py

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///sentences.db', echo=True)
Base = declarative_base()


class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "{}".format(self.name)


class Poem(Base):
    """"""
    __tablename__ = "poems"

    id = Column(Integer, primary_key=True)
    sentence = Column(String)

    title_id = Column(Integer, ForeignKey("titles.id"))
    title = relationship("Title", backref=backref(
        "poems", order_by=id))

# create tables
Base.metadata.create_all(engine)


