
# Gentle Journey website by Greg Khachaturyan
# This contains the routes and template processor code
# for each page. 


from flask import Flask, render_template, url_for, session
from html_editor.html_editor import *
from accounts.accounts import *

# These three lines instantiate the app and set the configuraiton
# directive for the Database and the secret key
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gj.db'
app.secret_key = 'giraffesandcatsaredabomb'

# These three lines register the accounts blueprint and 
# the html editor blueprint
app.register_blueprint(accounts, url_prefix='/edit')
app.register_blueprint(html_editor, url_prefix='/edit')
db.init_app(app)


# The root of the site. renders the home.html template and 
# retrieves all dynamically generated text from the database
# get_all_text() is located in html_editor.py
@app.route("/")
def index():
    return render_template('home.html', text=get_all_text())


# Renders the products page. This page is still in progress
@app.route("/products")
def products():
    return render_template("products.html")

# Pulls dynamic text from the database and sends it to 
# the services template where the template is rendered
@app.route("/services")
def services():
    waxing = Service.query.filter_by(tag="waxing").all()
    facials = Service.query.filter_by(tag="facial").all()
    return render_template("services.html", waxing=waxing, 
                           facials=facials, text=get_all_text())

# Simply renders the about page
@app.route("/about")
def about():
    return render_template("about.html", text=get_all_text())


# This route checks if the session has been set and redirects
# to login page or the index page depending
@app.route('/edit')
def edit():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return render_template('login.html',text=get_all_text())


# For testing purposes this runs the app from the command line
if __name__ == '__main__':
    app.debug = True
    app.run()
