

from flask import Flask, render_template,request,flash,session
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from wtforms import Form,  validators, StringField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired,ValidationError,DataRequired
from password import *
from flask_login import logout_user,LoginManager,login_required,login_user
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.exc import *
from functools import wraps
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:0270091294@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

migrate = Migrate(app, db)




class Data(db.Model):
    __tablename__="studentsignup"
    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(120))
    Lastname = db.Column(db.String(120))
    Email = db.Column(db.String(120),unique=True)
    Password = db.Column(db.String(120))
    Contact = db.Column(db.String(11))
    School = db.Column(db.String(120))
    Classification = db.Column(db.String(120))
    Major = db.Column(db.String(120))
    Gender = db.Column(db.String(120))



    def __init__(self,Firstname,Lastname,Email,Password,Contact,School,Classification,Major,Gender):
        self.Firstname = Firstname
        self.Lastname= Lastname
        self.Email = Email
        self.Password =Password
        self.Contact=Contact
        self.School=School
        self.Classification=Classification
        self.Major=Major
        self.Gender=Gender

    def is_active(self):
        return True


class Tutor(db.Model):
    __tablename__="tutorsignup"
    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(120))
    Lastname = db.Column(db.String(120))
    Email = db.Column(db.String(120),unique=True)
    Password = db.Column(db.String(120))
    Contact = db.Column(db.Integer)
    School = db.Column(db.String(120))
    Classification = db.Column(db.String(120))
    Major = db.Column(db.String(120))
    Gender = db.Column(db.String(120))
    Resume = db.Column(db.LargeBinary)
    Transcript = db.Column(db.LargeBinary)
    Classes = db.Column(db.String(120))
    Experience = db.Column(db.String(120))
    Expertise = db.Column(db.String(120))
    Reason = db.Column(db.String(120))
    Restriction = db.Column(db.String(120))

    def __init__(self,Firstname,Lastname,Email,Password,Contact,School,Classification,Major,Gender,Resume,Transcript,Classes,Experience,Expertise,Reason,Restriction):
        self.Firstname = Firstname
        self.Lastname= Lastname
        self.Email = Email
        self.Password =Password
        self.Contact=Contact
        self.School=School
        self.Classification=Classification
        self.Major=Major
        self.Gender=Gender
        self.Resume = Resume
        self.Transcript= Transcript
        self.Classes = Classes
        self.Experience = Experience
        self.Expertise = Expertise
        self.Reason = Reason
        self.Restriction = Restriction


class ReusableForm(Form):
    firstname = StringField('Name:', validators=[DataRequired()])
    lastname = StringField('Name:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired(), validators.Length(min=3, max=10),validators.EqualTo('cpassword', message='Passwords must match'),validators.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,10}$")])
    cpassword = PasswordField('Password:', validators=[DataRequired(), validators.Length(min=3, max=10)])
    contact = StringField('Name:', validators=[DataRequired()])
    school = StringField('Name:', validators=[DataRequired()])
    classification = StringField('Name:', validators=[DataRequired()])
    major = StringField('Name:', validators=[DataRequired()])
    gridRadios = StringField('Name:', validators=[DataRequired()])


@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/login",methods=["POST"])
def login():
    form = ReusableForm(request.form)
    if request.method == "POST" and form.validate():
        firstname =request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        password1 = hash_password(password)
        contact = request.form["contact"]
        school = request.form["school"]
        classification= request.form["classification"]
        major = request.form["major"]
        gender = request.form["gridRadios"]
        print(firstname,lastname,email,password1,contact,classification,major,school,gender)
        try:
            if db.session.query(Data).filter(Data.Email == email).count() == 0:

                data = Data(firstname, lastname, email, password1,contact,school,classification,major,gender)
                db.session.add(data)
                db.session.commit()
                flash("Documents succesfully submitted. You can now log into your account")
                return render_template("StudentReg.html",form=form, isIndex=True)

            else:
                flash("Email Already in use")
                render_template("StudentReg.html")
        except DataError:
            flash("Invalid data entry on contact. Enter 10 digits only")
            render_template("StudentReg.html")

        #flash("all filed required")
        #flash("Password must match confirm password")
        #return render_template("StudentReg.html", form=form)
    flash("all fields are required")
    flash("password must match confirm password")
    return render_template("StudentReg.html")

@app.route("/signup")
def signup():
    return render_template("StudentReg.html")


@app.route("/signedin",methods=["POST"])
def signedin():
    if request.method == "POST":
        email = request.form["studentemail"]
        pword = request.form["studentpassword"]
        print(pword)
        hashedpassword = db.session.query(Data.Password).filter(Data.Email == email).scalar()
        user = db.session.query(Data.Email).filter(Data.Email==email).scalar()


        if db.session.query(Data).filter(Data.Email == email).count() == 1 and check_password(hashedpassword,pword) == True:
            session["log"]=True
            flash("login success")
            return render_template("thanks.html")


        flash("Invalid Username and password")
        return render_template("welcome.html")




@app.route("/logout")

def logout():
    session.clear()
    flash("loggout succesfully")
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run(debug = True)