from application import app,db
from flask import render_template
from application.models import Login
from flask import request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.htm")

@app.route("/login", methods=['GET', 'POST'])
def login():
    name = ''
    password = ''
    email = ''
    if(request.method =='POST'):
        name=request.form.get('name')
        password=request.form.get('password')
        email=request.form.get('email')
    entry=Login(name=name, password=password,email=email)
    db.session.add(entry)
    db.session.commit()
    return render_template('login.htm')

if __name__=="__main__":
    app.run(debug=True)