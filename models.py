# -*- coding: utf-8 -*-
"""
Created on Tue May 19 03:30:47 2020

@author: Owner
"""

# models.py 

from app import db


class Title(db.Model):
    __tablename__ = "titles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}""".format(self.name)


class Poem(db.Model):
    """"""
    __tablename__ = "poems"

    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String)

    title_id = db.Column(db.Integer, db.ForeignKey("titles.id"))
    title = db.relationship("Title", backref=db.backref(
        "poems", order_by=id), lazy=True)

#</title:>
