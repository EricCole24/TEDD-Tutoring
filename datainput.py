from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from password import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:0270091294@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Data(db.Model):
    __tablename__="studentsignup"
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







@app.route("/")
def index():
    return render_template("StudentReg.html")


if __name__ == '__main__':
    app.run(debug = True)