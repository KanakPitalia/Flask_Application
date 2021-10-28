from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort,session,url_for,flash
# import sys
# print(sys.path)
# import ipdb
# ipdb.set_trace()
from flask_application import app
from datetime import datetime
import os
import pymysql

''' {% extends "public/templates/public_template.html" %}
    
     {% block title %}Home{% endblock %}
    
     {% block main %}
    
     <div class="container">
       <div class="row">
         <div class="col">
           <h1>Home</h1>
         </div>
       </div>
     </div>
    
    {% endblock %}'''


users = {
    "kanak__pitalia": {
        "name": "Kanak Pitalia",
        "bio": "IETian😇️😇️",
        "instagram_handle": "kanak__pitalia",
    },
    "satyam_mourya__": {
        "name": "Satyam Mourya",
        "bio": "",
        "instagram_handle": "satyam_mourya__"
    },
    "amiytiwari1": {
        "name": "Amiy Tiwari",
        "bio": "",
        "instagram_handle": "amiytiwari1"
    },
    "_mickayan_": {
        "name": "Narayan Sharma",
        "bio": "✨️✨️I'm the one at the sail, I'm the master of my sea...✨️✨️"
    }
}

connect = pymysql.connect(
    host="localhost", user=app.config["DB_USERNAME"], password=app.config["DB_PASSWORD"], db=None)
cur = connect.cursor()


def allowed_image(image):
    if "." not in image:
        return False
    split = image.split(".")
    if split[-1].upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/")
def index():
    cur.execute("use flask")
    output = cur.execute('''select * from Admin where username="dangi@12" and password="dani"''')
    print(output)

    return render_template("/public/index.html")


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/jinja")
def jinja():
    my_name = "Kanak Pitalia"
    my_age = 20
    langs = ["Python", "C++", "Java", "C"]
    date = datetime.utcnow()
    date = clean_date(date)
    return render_template("/public/jinja.html", my_name=my_name, my_age=my_age, langs=langs, date=date)


# @app.route("/sign-up", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         req = request.form
#         missing = []
#         for k, v in req.items():
#             if v == "":
#                 missing.append(k)
#         if missing:
#             f = f"Missing :- {' , '.join(missing)}"
#             return render_template("public/signup.html", feedback=f)
#         return redirect(request.url)
#     return render_template("public/signup.html")


@app.route("/profile")
def profile():

       
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        cur.execute(f"use {app.config['DB_NAME']}")
        cur.execute(f'''select * from profiles where Username="{username}"''')
        users=cur.fetchall()
        print(users)
        session["USERNAME"]=users[0][1]
        print("session username set")
        print(session)
        return render_template("public/profile.html",name=users[0][0],userName=users[0][1],email=users[0][2])
    else:
        print("No username found in session")
        return redirect(url_for("login"))


@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        response_body = {
            "message": "JSON received", "sender": req['name']
        }
        res = make_response(jsonify(response_body), 200)
        return res
    response_body = {
        "message": "JSON required"
    }
    res = make_response(jsonify(response_body), 400)
    return res


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)
    res = make_response(jsonify(req), 200)
    return res


@app.route("/query")
def query():
    args = request.args
    # print(args)
    a = []
    for v in args.values():
        a.append(v)

    return "<br>".join(a)


@app.route("/upload-image", methods=["POST", "GET"])
def upload_image():
    if request.method == "POST":
        if request.files:
            images = request.files.getlist("image")
            for image in images:

                if image.filename == "":
                    print("No Filename")
                    return redirect(request.url)
                else:
                    if allowed_image(image.filename):

                        image.save(os.path.join(
                            app.config["IMAGE_UPLOADS"], image.filename))
                        print("Image Saved",image.filename)
                    else:
                        print("That file extension is not allowed")
                        break
                        return redirect(request.url)
            return redirect(request.url)
            
    return render_template("public/upload_image.html")


@app.route("/get-image/<image_name>")
def get_image(image_name):
    flag = 0
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], image_name)
    except FileNotFoundError:
        abort(404)
        # print("Sorry your file not found,either it is replaced with different name or it is permanently moved on to different directory!")


@app.route("/get-csv/<csv_id>")
def get_csv(csv_id):
    filename = f"{csv_id}.csv"
    try:
        return send_from_directory(app.config["CLIENT_CSV"], filename)
    except FileNotFoundError:
        abort(404)


@app.route("/get-pdf/<pdf_id>")
def get_pdf(pdf_id):
    filename = f"{pdf_id}.pdf"
    try:
        return send_from_directory(app.config["CLIENT_PDF"], filename)
    except FileNotFoundError:
        abort(404)


@app.route("/cookies")
def cookies():
    res = make_response("cookies")
    print(request.cookies)
    res.set_cookie("Name", "Kanak Pitalia", max_age=10, path=request.path)
    return res
    # cookies=request.cookies


@app.route("/login", methods=["GET", "POST"])
def login():
    checked="checked"
    unchecked="unchecked"
    if request.method == "POST":
        username = request.form.get("UserName")
        password = request.form.get("Password")
        print(f"Username = {username},Password = {password}")
        containsDatabase = cur.execute(f"show databases LIKE '{app.config['''DB_NAME''']}'")
        print(containsDatabase)
        if containsDatabase:
            cur.execute(f"use {app.config['DB_NAME']}")
            containsTable = cur.execute("show tables LIKE 'profiles'")
            print("Tables =",containsTable)
            if containsTable:
                ide=check(username, password)
                print(ide)
                if ide==(1,1):
                    session["USERNAME"]=username
                    return redirect(url_for('profile',))
                elif ide==(1,0):
                    flash("Password is incorrect!","danger")
                    # feedback = "Password is incorrect!"
                    print(session)
                    return render_template("public/loginSignup.html",login=checked,signup=unchecked)
                else:
                    flash('You\'re not the user,sign-up first',"danger")
                    # feedback = 'You\'re not the user,sign-up first'
                    print(session)
                    return render_template("/public/loginSignup.html",login=unchecked,signup=checked)
        # return redirect(render_template("public/loginsignup.html",login=checked,signup=unchecked)
            # else:
            #     cur.execute("CREATE TABLE profiles(Name VARCHAR(50) NOT NULL,Username VARCHAR(50) NOT NULL,Email VARCHAR(50) NOT NULL,Password VARCHAR(50) NOT NULL,PRIMARY KEY (Username));")
    
    return render_template("public/loginSignup.html",login=checked,signup=unchecked)
def check(username, password):
    
    output=cur.execute(f'''select * from profiles where username="{username}"''')
    output=cur.fetchall()
    # print("user and password =",output)
    if output:
        if output[0][1]==username and output[0][3]==password:
            return 1,1
        elif output[0][1]==username and output[0][3]!=password:
            return 1,0
    else:
        return 0,0

@app.route("/sign-out")
def signout():
    session.pop("USERNAME",None)
    print(session)
    return redirect(url_for("login"))

@app.route("/sign-up",methods=["POST"])
def signup():
    checked="checked"
    unchecked="unchecked"
    if request.method=="POST":
        username=request.form.get("UserName")
        name=request.form.get("Name")
        email=request.form.get("Email")
        password=request.form.get("Password")
        if not len(password)>=10:
            flash("Password must be of atleast 10 characters","warning")
            print(session)
            return render_template("/public/loginSignup.html",login=unchecked,signup=checked)
        print(f"Username = {username},Password = {password},Email = {email},Name = {name}")
        containsDatabase = cur.execute(f"show databases LIKE '{app.config['''DB_NAME''']}'")
        print(containsDatabase)
        if containsDatabase:
            cur.execute(f"use {app.config['DB_NAME']}")
            containsTable = cur.execute("show tables LIKE 'profiles'")
            print("Tables =",containsTable)
            if containsTable:
                adduser(name,username,email,password)
                flash("Account created!","success")
                print(session)
                return redirect(url_for("login"))
            else:
                cur.execute("CREATE TABLE profiles(Name VARCHAR(50) NOT NULL,Username VARCHAR(50) NOT NULL,Email VARCHAR(50) NOT NULL,Password VARCHAR(50) NOT NULL,PRIMARY KEY (Username));")
                adduser(name, username, email, password)
                return redirect(url_for("login"))
        else:
            cur.execute(f"create database {app.config['DB_NAME']}")
            cur.execute(f"use {app.config['DB_NAME']}")
            cur.execute("CREATE TABLE profiles(Name VARCHAR(50) NOT NULL,Username VARCHAR(50) NOT NULL,Email VARCHAR(50) NOT NULL,Password VARCHAR(50) NOT NULL,PRIMARY KEY (Username));")
            adduser(name, username, email, password)
            return redirect(url_for("login"))
    return redirect(url_for("login"))

def adduser(name,username,email,password):
    cur.execute(f'''INSERT INTO profiles VALUES("{name}","{username}","{email}","{password}");''')
    connect.commit()
    return 0

# @app.errorhandler(404)
# def page_not_found(e):
#     app.logger.info(f"Page Not Found :{request.url}")
#     return f"Hello guys :{e}",404

@app.errorhandler(500)
def server_error(e):
    # email_admin(message = "Server error",url=request.url,error=e)
    app.logger.error("Server is not working properly")
    return f"Sorry for the inconvenient cause! \n {e}",500

