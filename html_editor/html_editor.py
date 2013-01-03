
# This Blueprint has functions and routes for handling Ajax 
# requests from the client to add, delete, and update data from
# the database for misclaneous dynamic html and for services.

import traceback
from flask import Blueprint, render_template, url_for, request, redirect
from text_model import *
from service_model import *

# Defines html_editor as a blueprint
html_editor = Blueprint('html_editor', __name__,
                        template_folder='templates',
                        static_folder='stat')


# This retrieves all the data from the Text table
# and returns it as an object with each row equal to
# a property
def get_all_text():
    text_content = {}
    all_text = Text.query.all()

    for item in all_text:
        text_content[item.tag] = item.text

    return text_content

# This is an example for testing purposes. It renders and populates
# the template with dynamic text
@html_editor.route("/edit_example")
def edit_example():
    text = Text.query.all()
    return render_template('edit.html', text=text)


# This route and function update data in the 
# Text table
@html_editor.route('/update_text', methods=['POST'])
def update_text():
    if request.method == 'POST':
        text = request.form['text']
        tag = request.form['tag']

        text_query = Text.query.filter_by(tag=tag).first()
        if (text_query != None):
            text_query.text = text
            db.session.commit()

        else:
            text_entry = Text(text, tag)
            db.session.add(text_entry)
            db.session.commit()

        return "success"

# This function and route add, delete and update entries 
# in the services table. It expects an action from 
# ajax sent via POST. 
@html_editor.route('/edit_service', methods=['POST'])
def edit_service():
    if (request.method == 'POST'):
        title = ""
        body = ""
        price = ""
        tag = "notag"
        action =""
        
        try:
            title = request.form['title']
        except:
            pass

        try:
            body = request.form['body']
        except:
            pass
                
        try:
            price = request.form['price']
        except:
            pass

        try:
            tag = request.form['tag']
        except:
            pass
        
        try:
            action = request.form['action']
        except:
            pass

        if (action == "add"):
            service = Service(title,body,price,tag)
            db.session.add(service)
            db.session.commit()
        
        elif (action == 'edit'):
            id = request.form['id']
            service = Service.query.filter_by(id=id).first()
            service.title = title
            service.body = body
            service.price = price
            db.session.commit()
        
        elif (action == 'delete'):
            id = request.form['id']
            service = Service.query.filter_by(id=id).first()
            db.session.delete(service)
            db.session.commit()

        else:
            print "No action specified"
        

    
    return redirect(url_for('services'))
