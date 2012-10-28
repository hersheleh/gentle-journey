from flask import Flask, render_template, url_for, session
from accounts.accounts import *

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gj.db'
app.secret_key = 'giragesandcatsaredabomb'

app.register_blueprint(accounts, url_prefix='/edit')
db.init_app(app)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/edit')
def edit():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('accounts.login'))


if __name__ == '__main__':
    app.debug = True
    app.run()

