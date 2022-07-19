# -*- coding: utf-8 -*-
"""
Created on Tue May 19 05:54:44 2020

@author: Owner
"""

# forms.py

from wtforms import Form, StringField, SelectField

class SentenceSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Poem', 'Poem')]
    select = SelectField('Search for poems:', choices=choices)
    search = StringField('')
    
class PoemForm(Form):
    title = StringField('Title')
    sentence = StringField('Sentence')
