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
    return render_template('index.html')

@app.route('/person')
def person():
    roles = Role.query.all()
    shifts = Shift.query.all()
    persons = Person.query.all()
    groups = Group.query.all()
    return render_template('index.html', persons=persons, roles=roles, shifts=shifts, groups=groups)

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
        role = form.get('role')
        group = form.get('group')
        shift = form.get('shift')
        is_active = True
        if person_id:
            person = Person.query.get(person_id)
            if person:
                db.session.delete(person)
                db.session.commit()
        
        if not fname or lname or email or username:
            if person_id:
                person = Person(person_id = person_id, fname = fname, lname = lname, email = email, username = username, is_active = is_active, group = group, role = role, shift = shift)
            else:
                person = Person(fname = fname, lname = lname, email = email, username = username, is_active = is_active, group = group, role = role, shift = shift)
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
            if role_id:
                role = Role(role_id = role_id, name = name)
            else:
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
        start_hour = form.get('start_hour')
        end_hour = form.get('end_hour')
        if form.get('sunday') == "true":
            sunday = True
        else:
            sunday = False
        if form.get('monday') == "true":
            monday = True
        else:
            monday = False
        if form.get('tuesday') == "true":
            tuesday = True
        else:
            tuesday = False
        if form.get('wednesday') == "true":
            wednesday = True
        else:
            wednesday = False
        if form.get('thursday') == "true":
            thursday = True
        else:
            thursday = False
        if form.get('friday') == "true":
            friday = True
        else:
            friday = False
        if form.get('saturday') == "true":
            saturday = True
        else:
            saturday = False
        shift_id = form.get('shift_id')
        if shift_id:
            shift = Shift.query.get(shift_id)
            if shift:
                db.session.delete(shift)
                db.session.commit()

        if not name or start_hour or end_hour or sunday or monday or tuesday or wednesday or thursday or friday or saturday:
            if shift_id:
                shift = Shift(shift_id = shift_id, name = name, start_hour = start_hour, end_hour = end_hour, sunday = sunday, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday)
            else:
                shift = Shift(name = name, start_hour = start_hour, end_hour = end_hour, sunday = sunday, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday)
            db.session.add(shift)
            db.session.commit()
            return redirect('/shift')

    return "of the jedi"

@app.route('/add_group', methods=['POST'])
def add_group():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        group_id = form.get('group_id')
        if group_id:
            group = Group.query.get(group_id)
            if group:
                db.session.delete(group)
                db.session.commit()

        if name:
            if group_id:
                group = Group(group_id = group_id, name = name)
            else:
                group = Group(name = name)
            db.session.add(group)
            db.session.commit()
            return redirect('/group')

    return "of the jedi"

#update routes
@app.route('/update_person/<int:id>')
def update_person(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            return render_template('update_person.html', person=person)

    return "of the jedi"

@app.route('/update_role/<int:id>')
def update_role(id):
    if not id or id != 0:
        role = Role.query.get(id)
        if role:
            return render_template('update_role.html', role=role)

    return "of the jedi"

@app.route('/update_group/<int:id>')
def update_group(id):
    if not id or id != 0:
        group = Group.query.get(id)
        if group:
            return render_template('update_group.html', group=group)

    return "of the jedi"

@app.route('/update_shift/<int:id>')
def update_shift(id):
    if not id or id != 0:
        shift = Shift.query.get(id)
        if shift:
            return render_template('update_shift.html', shift=shift)

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

@app.route('/delete_shift/<int:id>')
def delete_shift(id):
    if not id or id != 0:
        shift = Shift.query.get(id)
        if shift:
            db.session.delete(shift)
            db.session.commit()
        return redirect('/shift')

    return "of the jedi"

@app.route('/delete_group/<int:id>')
def delete_group(id):
    if not id or id != 0:
        group = Group.query.get(id)
        if group:
            db.session.delete(group)
            db.session.commit()
        return redirect('/group')

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
