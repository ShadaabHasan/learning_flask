from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='eef1fb5493da5807e062c887cb7127f0'

posts=[
    {
        'author': 'Shadaab Hasan',
        'title':'Blog Post 1',
        'content':'My first post!',
        'date_posted':'29th August 2023'
    },
    {
        'author': 'Jia Thakkar',
        'title':'Blog Post 2',
        'content':'My first post!!',
        'date_posted':'29th August 2023'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', new_addition=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form= RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form= LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)