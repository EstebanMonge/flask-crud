from flask import render_template, request, redirect
from app import app, db
from app.models import Person
from app.models import Group
from app.models import Role 
from app.models import Shift 

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    persons = Person.query.all()
    return render_template('index.html', persons=persons)

@app.route('/person')
def person():
    persons = Person.query.all()
    return render_template('index.html', persons=persons)

@app.route('/role')
def role():
    role = Role.query.all()
    return render_template('index.html', role=role)

@app.route('/group')
def group():
    group = Group.query.all()
    return render_template('index.html', group=group)

@app.route('/shift')
def shift():
    shift = Shift.query.all()
    return render_template('index.html', shift=shift)

@app.route('/add_person', methods=['POST'])
def add():

    if request.method == 'POST':
        form = request.form
        fname = form.get('fname')
        lname = form.get('lname')
        email = form.get('email')
        username = form.get('username')
        person_id = form.get('person_id')
        is_active = True
        if person_id:
            person = Person.query.get(person_id)
            if person:
                db.session.delete(person)
                db.session.commit()
        
        if not fname or lname or email or username:
            person = Person(fname = fname, lname = lname, email = email, username = username, is_active = is_active)
            db.session.add(person)
            db.session.commit()
            return redirect('/person')

    return "of the jedi"

@app.route('/update_person/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            return render_template('update_person.html', person=person)

    return "of the jedi"

@app.route('/delete_person/<int:id>')
def delete(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            db.session.delete(person)
            db.session.commit()
        return redirect('/person')

    return "of the jedi"

@app.route('/turn_person/<int:id>')
def turn(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            person.is_active = not person.is_active
            db.session.commit()
        return redirect('/person')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"
