from flask import render_template, request, redirect
from app import app, db
from app.models import Person
from app.models import Group
from app.models import Role 
from app.models import Shift 

jedi = "of the jedi"

#display routes
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
    roles = Role.query.all()
    return render_template('index.html', roles=roles)

@app.route('/group')
def group():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)

@app.route('/shift')
def shift():
    shifts = Shift.query.all()
    return render_template('index.html', shifts=shifts)

#add routes
@app.route('/add_person', methods=['POST'])
def add_person():
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

@app.route('/add_role', methods=['POST'])
def add_role():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        role_id = form.get('role_id')
        if role_id:
            role = Role.query.get(role_id)
            if role:
                db.session.delete(role)
                db.session.commit()

        if name:
            role = Role(name = name)
            db.session.add(role)
            db.session.commit()
            return redirect('/role')

    return "of the jedi"

@app.route('/add_shift', methods=['POST'])
def add_shift():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        shift_id = form.get('shift_id')
        if shift_id:
            shift = Shift.query.get(shift_id)
            if shift:
                db.session.delete(shift)
                db.session.commit()

        if name:
            shift = Shift(name = name)
            db.session.add(shift)
            db.session.commit()
            return redirect('/shift')

    return "of the jedi"

@app.route('/update_person/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            return render_template('update_person.html', person=person)

    return "of the jedi"

#delete routes
@app.route('/delete_person/<int:id>')
def delete_person(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            db.session.delete(person)
            db.session.commit()
        return redirect('/person')

    return "of the jedi"

@app.route('/delete_role/<int:id>')
def delete_role(id):
    if not id or id != 0:
        role = Role.query.get(id)
        if role:
            db.session.delete(role)
            db.session.commit()
        return redirect('/role')

    return "of the jedi"

@app.route('/turn_person/<int:id>')

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
