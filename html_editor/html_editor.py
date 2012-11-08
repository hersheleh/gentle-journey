from flask import Blueprint, render_template, url_for, request, redirect
from text_model import *
from service_model import *

html_editor = Blueprint('html_editor', __name__,
                        template_folder='templates',
                        static_folder='stat')


@html_editor.route("/edit_example")
def edit_example():
    text = Text.query.all()
    return render_template('edit.html', text=text)


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

@html_editor.route('/edit_service', methods=['POST'])
def edit_service():
    title = request.form['title']
    body = request.form['body']
    price = request.form['price']
    tag = request.form['tag']
    action = request.form['action']
    
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
        
    elif(action == 'delete'):
        id = request.form['id']
        sevice = Service.query.filter_by(id=id).first()
        db.session.delete(service)
        db.session.commit()
        
    return redirect(url_for('services'))
