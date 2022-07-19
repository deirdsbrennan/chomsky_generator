# -*- coding: utf-8 -*-
"""
Created on Tue May 19 03:36:30 2020

@author: Owner
"""

# main.py

from app import app
from db_setup import init_db, db_session
from forms import SentenceSearchForm, PoemForm
from flask import flash, render_template, request, redirect
from models import Poem, Title
from tables import Results
from chomsky_generator import generate
import time

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = SentenceSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    #search in the title or sentence field depending on
    #selection
    if search_string:
        if search.data['select'] == 'Title':
            qry = db_session.query(Poem, Title).filter(
                Title.id==Poem.title_id).filter(
                    Title.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Poem':
            qry = db_session.query(Poem).filter(
                Poem.sentence.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Poem)
            results = qry.all()
    else:
        qry = db_session.query(Poem)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_poem', methods=['GET', 'POST'])
def new_poem():
    """
    Add a new poem
    """
    #newSentence = 'this is test 2'#generate()
    #newPoem = {'title': '', 'sentence': newSentence}
    
    form = PoemForm(request.form)

    if request.method == 'POST' and form.validate():
        if "submit_button" in request.form:
            # save the poem
            poem = Poem()
            save_changes(poem, form, new=True)
            flash('Poem created successfully!')
            return redirect('/')
        elif "generate_button" in request.form:
            newSentence = generate()
            flash(newSentence)
            return redirect('/new_poem')

    return render_template('new_poem.html', form=form)

def save_changes(poem, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    title = Title()
    title.name = form.title.data

    poem.title = title
    poem.sentence = form.sentence.data

    if new:
        # Add the new poem to the database
        db_session.add(poem)

    # commit the data to the database
    db_session.commit()
    
@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Poem).filter(
                Poem.id==id)
    poem = qry.first()

    if poem:
        form = PoemForm(formdata=request.form, obj=poem)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(poem, form)
            flash('Poem updated successfully!')
            return redirect('/')
        return render_template('edit_poem.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
#</int:id>
        
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Poem).filter(
        Poem.id==id)
    poem = qry.first()

    if poem:
        form = PoemForm(formdata=request.form, obj=poem)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(poem)
            db_session.commit()

            flash('Poem deleted successfully!')
            return redirect('/')
        return render_template('delete_poem.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)
#</int:id>

if __name__ == '__main__':
    app.run()

