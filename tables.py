# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:40:32 2020

@author: Owner
"""

from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    sentence = Col('Sentence')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

