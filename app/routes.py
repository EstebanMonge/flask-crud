import os
import pandas as pd
from flask import render_template, request, redirect
from app import app, db
from app.models import Person
from app.models import Group
from app.models import Role 
from app.models import Shift 
from app.models import Platform 
from app.models import Handover
from app.models import Chat 

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
    platforms = Platform.query.all()
    return render_template('index.html', persons=persons, roles=roles, shifts=shifts, groups=groups, platforms=platforms)

@app.route('/handover')
def handover():
    handovers = Handover.query.all()
    persons = Person.query.all()
    platforms = Platform.query.all()
    return render_template('index.html', handovers=handovers, persons=persons, platforms=platforms)

@app.route('/chat')
def chat():
    chats = Chat.query.all()
    return render_template('index.html', chats=chats)


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

@app.route('/platform')
def platform():
    platforms = Platform.query.all()
    return render_template('index.html', platforms=platforms)

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
        platform = form.get('platform')
        is_active = True
        if person_id:
            person = Person.query.get(person_id)
            if person:
                db.session.delete(person)
                db.session.commit()
        
        if not fname or lname or email or username:
            if person_id:
                person = Person(person_id = person_id, fname = fname, lname = lname, email = email, username = username, is_active = is_active, group = group, role = role, shift = shift, platform=platform)
            else:
                person = Person(fname = fname, lname = lname, email = email, username = username, is_active = is_active, group = group, role = role, shift = shift, platform=platform)
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

@app.route('/add_platform', methods=['POST'])
def add_platform():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        platform_id = form.get('platform_id')
        if platform_id:
            platform = Platform.query.get(platform_id)
            if role:
                db.session.delete(platform)
                db.session.commit()

        if name:
            if platform_id:
                platform = Platform(platform_id = platform_id, name = name)
            else:
                platform = Platform(name = name)
            db.session.add(platform)
            db.session.commit()
            return redirect('/platform')

    return "of the jedi"

@app.route('/add_handover', methods=['POST'])
def add_handover():
    if request.method == 'POST':
        form = request.form
        ho_id = form.get('ho_id')
        ticket = form.get('ticket')
        ticket_type = form.get('ticket_type')
        servers = form.get('servers')
        platform = form.get('platform')
        steps = form.get('steps')
        next_steps = form.get('next_steps')
        chat_url = form.get('chat_url')
        owner = form.get('owner')
        old_owners = form.get('old_owners')
        is_active = True
        if ho_id:
            ho = Handover.query.get(ho_id)
            if role:
                db.session.delete(ho)
                db.session.commit()

        if not ticket or ticket_type or servers or steps or next_steps or chat_url or owner or old_owners:
            if ho_id:
                handover = Handover(ho_id = ho_id, ticket = ticket, ticket_type = ticket_type, servers = servers, platform=platform, steps = steps, next_steps = next_steps, chat_url = chat_url, owner = owner, old_owners = old_owners, is_active = is_active) 
            else:
                handover = Handover(ticket = ticket, ticket_type = ticket_type, servers = servers, platform = platform, steps = steps, next_steps = next_steps, chat_url = chat_url, owner = owner, old_owners = old_owners, is_active = is_active) 
            db.session.add(handover)
            db.session.commit()
            return redirect('/handover')

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

@app.route('/add_chat', methods=['POST'])
def add_chat():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        chat_url = form.get('chat_url')
        chat_id = form.get('chat_id')
        if chat_id:
            chat = Chat.query.get(chat_id)
            if chat:
                db.session.delete(chat)
                db.session.commit()

        if name:
            if chat_id:
                chat =Chat(chat_id = chat_id, name = name, chat_url = chat_url)
            else:
                chat = Chat(name = name, chat_url = chat_url)
            db.session.add(chat)
            db.session.commit()
            return redirect('/chat')

    return "of the jedi"

#update routes
@app.route('/update_person/<int:id>')
def update_person(id):
    if not id or id != 0:
        person = Person.query.get(id)
        roles = Role.query.all()
        groups = Group.query.all()
        shifts = Shift.query.all()
        platforms = Platform.query.all()
        if person:
            return render_template('update_person.html', person=person, roles=roles, groups=groups, shifts=shifts, platforms=platforms)

    return "of the jedi"

@app.route('/update_chat/<int:id>')
def update_chat(id):
    if not id or id != 0:
        chat = Chat.query.get(id)
        if chat:
            return render_template('update_chat.html', chat=chat)

    return "of the jedi"

@app.route('/update_platform/<int:id>')
def update_platform(id):
    if not id or id != 0:
        platform = Platform.query.get(id)
        if platform:
            return render_template('update_platform.html', platform=platform)

    return "of the jedi"

@app.route('/update_handover/<int:id>')
def update_handover(id):
    if not id or id != 0:
        handover = Handover.query.get(id)
        platforms = Platform.query.all()
        persons = Person.query.all()
        if handover:
            return render_template('update_handover.html', handover=handover, platforms=platforms, persons=persons)

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

@app.route('/delete_chat/<int:id>')
def chat_person(id):
    if not id or id != 0:
        chat = Chat.query.get(id)
        if chat:
            db.session.delete(chat)
            db.session.commit()
        return redirect('/chat')

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

@app.route('/delete_platform/<int:id>')
def delete_platform(id):
    if not id or id != 0:
        platform = Platform.query.get(id)
        if platform:
            db.session.delete(platform)
            db.session.commit()
        return redirect('/platform')

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

@app.route('/delete_handover/<int:id>')
def delete_handover(id):
    if not id or id != 0:
        handover = Handover.query.get(id)
        if handover:
            db.session.delete(handover)
            db.session.commit()
        return redirect('/handover')

    return "of the jedi"

@app.route('/turn_person/<int:id>')
def turn_person(id):
    if not id or id != 0:
        person = Person.query.get(id)
        if person:
            person.is_active = not person.is_active
            db.session.commit()
        return redirect('/person')

    return "of the jedi"

@app.route('/turn_handover/<int:id>')
def turn_handover(id):
    if not id or id != 0:
        handover = Handover.query.get(id)
        if handover:
            handover.is_active = not handover.is_active
            db.session.commit()
        return redirect('/handover')

    return "of the jedi"

@app.route("/import_person", methods=['POST'])
def import_person():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
      return redirect('/person')

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['fname','lname','email', 'username', 'is_active' , 'role', 'platform', 'shift', 'group']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=0)
      # Loop through the Rows
      for i,row in csvData.iterrows():
           person = Person(fname = row['fname'], lname = row['lname'], email = row['email'], username = row['username'] , is_active = row['is_active'], group = row['group'], role = row['role'], shift = row['shift'], platform=row['platform'])
           db.session.add(person)
           db.session.commit()
      return redirect('/person')

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"
