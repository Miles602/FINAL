import errno
from gzip import READ
from os import abort
from flask import Flask, redirect, render_template, request, url_for
from src.repositories.user_repository import user_repository_singleton
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2020@localhost:3306/forum'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Homepage link
@app.get('/')
def index():
    return render_template('index.html')

#Post Link
@app.get('/post/new')
def post_form():
    return render_template('post.html')

@app.post('/post')
def post():
    post_title=request.form.get('title','')
    post_comment=request.form.get('post_text','')

    if post_title =='' or post_comment=='':
        abort(400)
    new_post=user_repository_singleton.create_post(post_title,post_comment)
    return redirect(f'/post/{new_post.post_id}')

#Login link
@app.route('/login', methods=["GET","POST"])
def login():
    error = None

    #if request.method =='POST':
        #if request.form['username'] != 'admin' or request.form["password"] != "admin":
            #error="invalid resonse, please try again"
        #else:
            #return redirect('/')

    if request.method =='POST':
        username = request.form.get('username', '')
        passcode = request.form.get('passcode', '')
        is_user = user_repository_singleton.login(username, passcode)

        if is_user != True:
            error = 'Invalid response, please try again.'
        else:
            return redirect('/')

    return render_template("login.html",error = error)

#Register link
@app.get('/register/new')
def register_form():
    return render_template("registration.html")

@app.post('/register')
def register():
    error = None
    username = request.form.get('username', '')
    passcode = request.form.get('passcode', '')

    if username == '' or passcode == '':
        error = 'You have not filled in your information'
    else:
        created_user = user_repository_singleton.create_user(username, passcode)
        return redirect('/')

    return render_template('registration.html', error = error)


@app.get('/post/search')
def search_for_forum():
    found_posts=[]
    search_term= request.args.get('forumsearch','')
    if search_term != '':
        found_posts=user_repository_singleton.search_post(search_term)

    return render_template('search.html',search_active=True,posts=found_posts,search_query=search_term)

@app.get("/post/<int:post_id>")
def get_single_post(post_id):
    single_post=user_repository_singleton.get_post_by_id(post_id)
    return render_template('get_post.html',post=single_post)





    
if __name__ == '__main__':
    app.run()