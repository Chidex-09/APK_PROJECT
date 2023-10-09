# This is to import flask 
from flask import Flask, render_template, request

#..

# This is to stage the application
app = Flask(__name__)

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get("username")
        PASSWORD = request.form.get("PASSWORD")  
        phone_number = request.form.get("number") 
        new_user = {"username":username,
                    "password":PASSWORD,
                    "phone_number":phone_number}
        print (new_user)
        
    return render_template("index.html")
                
        
#..

# This is to define your route
@app.route('/')
def homepage():
    return render_template("Welcome.html")

@app.route('/login')
def login():
    return render_template("login.html")

#this is the bottom of the flask

if __name__ == "__main__":
    app.run(debug=True)