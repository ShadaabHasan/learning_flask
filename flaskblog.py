from flask import Flask, render_template
app = Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)