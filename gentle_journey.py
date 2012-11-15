
from flask import Flask, render_template, url_for, session
from html_editor.html_editor import *
from accounts.accounts import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gj.db'
app.secret_key = 'giraffesandcatsaredabomb'

app.register_blueprint(accounts, url_prefix='/edit')
app.register_blueprint(html_editor, url_prefix='/edit')
db.init_app(app)


@app.route("/")
def index():
    return render_template('home.html', text=get_all_text())


@app.route("/services")
def services():
    waxing = Service.query.filter_by(tag="waxing").all()
    facials = Service.query.filter_by(tag="facial").all()
    return render_template("services.html", waxing=waxing, 
                           facials=facials, text=get_all_text())


@app.route("/about")
def about():
    return render_template("about.html", text=get_all_text())


@app.route('/edit')
def edit():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('accounts.login'))


if __name__ == '__main__':
    app.debug = True
    app.run()
