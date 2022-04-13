import errno
from gzip import READ
from os import abort
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET","POST"])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] != 'admin' or request.form["password"] != "admin":
            error="invalid resonse, please try again"
        else:
            return redirect('/')

    return render_template("login.html",error=error)


@app.get('/register/new')

def register_form():
    return render_template("registration.html")


@app.post('/register')
def register():
    error=None
    user_name=request.form.get('username','')
    password=request.form.get("password",'') # Try to stick to either double or single quotes for consistency
    if user_name == '' or password=='':
            error="You have not filled in your information"
    else:
        return redirect("/")
    return render_template("registration.html",error=error)
    





if __name__ == '__main__':
    app.run()