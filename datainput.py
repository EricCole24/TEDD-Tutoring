
from datetime import datetime
from datetime import timedelta
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_sqlalchemy import SQLAlchemy
from pip._vendor import requests
from sqlalchemy.exc import *
from wtforms import Form, validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
import emailing
from password import *
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import threading








import os

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0270091294@localhost/students'

#app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://suycphndnkunkv:2619b47f59858a9d3849834c1ff425d7c237a8626f3dca0da805bb6033b5ef75@ec2-107-20-230-70.compute-1.amazonaws.com:5432/dc7hidu3ph7idk?sslmode=require'

app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://yoogwgjgkgmuzf:b0e8d86313ed45178f710cdb2006da017f0e64e42ef685f350385c931ba0758b@ec2-174-129-254-226.compute-1.amazonaws.com:5432/d104c2unu0s8ni?sslmode=require'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0270091294@localhost/students'

#app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://suycphndnkunkv:2619b47f59858a9d3849834c1ff425d7c237a8626f3dca0da805bb6033b5ef75@ec2-107-20-230-70.compute-1.amazonaws.com:5432/dc7hidu3ph7idk?sslmode=require'

#app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://yoogwgjgkgmuzf:b0e8d86313ed45178f710cdb2006da017f0e64e42ef685f350385c931ba0758b@ec2-174-129-254-226.compute-1.amazonaws.com:5432/d104c2unu0s8ni?sslmode=require'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
#app.config['WHOOSH_BASE']='whoosh'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"
migrate = Migrate(app, db)
user_datastore = SQLAlchemy

csrf = CSRFProtect(app)
admin = Admin(app)

sentry_sdk.init(
    dsn="https://990d5ad8be404b839c7441234bae2fef@sentry.io/1871585",
    integrations= [FlaskIntegration(),SqlalchemyIntegration()]
)





app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)


class Data(db.Model, UserMixin):
    __tablename__= "studentsignup"
    id = db.Column(db.Integer, primary_key = True)
    Firstname = db.Column(db.String(120))
    Lastname = db.Column(db.String(120))
    Email = db.Column(db.String(120),unique = True)
    Password = db.Column(db.String(120))
    Contact = db.Column(db.String(11))
    School = db.Column(db.String(120))
    Classification = db.Column(db.String(120))
    Major = db.Column(db.String(120))
    Gender = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean,default=False)
    Role = db.relationship('StudentData',backref ='user', lazy = True)
    Role2 = db.relationship('Post', backref='user', lazy=True)


    def __init__(self, Firstname: object, Lastname: object, Email: object, Password: object, Contact: object, School: object, Classification: object, Major: object, Gender: object) :
        self.Firstname = Firstname
        self.Lastname= Lastname
        self.Email = Email
        self.Password = Password
        self.Contact = Contact
        self.School = School
        self.Classification = Classification
        self.Major = Major
        self.Gender = Gender


    def is_active(self):
        return True

class StudentData(db.Model):
    __tablename__ = "schedulesignup"
    id = db.Column(db.Integer, primary_key = True)
    Preferedname = db.Column(db.String(120))
    Classes = db.Column(db.String(120))
    Day = db.Column(db.String(120))
    Date = db.Column(db.Date())
    Time = db.Column(db.Time())
    Taken = db.Column(db.String(120))
    Areas = db.Column(db.String(120))
    Comment = db.Column(db.String(120))
    data_id = db.Column(db.Integer,db.ForeignKey('studentsignup.id'))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)


    def __init__(self, Preferedname, Classes, Day, Date, Time, Taken, Areas, Comment, data_id):
        self.Preferedname = Preferedname
        self.Classes = Classes
        self.Taken = Taken
        self.Areas = Areas
        self.Comment = Comment
        self.Day = Day
        self.Date = Date
        self.Time = Time
        self.data_id = data_id


class Tutor(db.Model):
    __tablename__= "tutorsignup"
    id = db.Column(db.Integer, primary_key = True)
    Firstname = db.Column(db.String(120))
    Lastname = db.Column(db.String(120))
    Email = db.Column(db.String(120),unique = True)
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

    def __init__(self, Firstname, Lastname, Email, Password, Contact, School, Classification, Major, Gender, Resume,
                 Transcript, Classes, Experience, Expertise, Reason, Restriction):
        self.Firstname = Firstname
        self.Lastname= Lastname
        self.Email = Email
        self.Password = Password
        self.Contact = Contact
        self.School = School
        self.Classification = Classification
        self.Major = Major
        self.Gender = Gender
        self.Resume = Resume
        self.Transcript = Transcript
        self.Classes = Classes
        self.Experience = Experience
        self.Expertise = Expertise
        self.Reason = Reason
        self.Restriction = Restriction

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    Body = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    Title = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('studentsignup.id'))

    def __init__(self,Body,Title,user_id):
        self.Body = Body
        self.Title = Title
        self.user_id = user_id





class ReusableForm(Form):
    firstname = StringField('Name:', validators = [DataRequired()])
    lastname = StringField('Name:', validators = [DataRequired()])
    email = EmailField('Email:', validators = [validators.DataRequired()])
    password = PasswordField('Password:', validators = [DataRequired(), validators.Length(min = 3, max = 10),validators.EqualTo('cpassword', message = 'Passwords must match'),validators.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,10}$")])
    cpassword = PasswordField('Password:', validators = [DataRequired(), validators.Length(min = 3, max = 10)])
    contact = StringField('Name:', validators = [DataRequired()])
    school = StringField('Name:', validators = [DataRequired()])
    classification = StringField('Name:', validators = [DataRequired()])
    major = StringField('Name:', validators = [DataRequired()])
    gridRadios = StringField('Name:', validators = [DataRequired()])


class StudentForm(Form):
    pname = StringField('Name:', validators = [DataRequired()])
    textarea1 = StringField('Name:', validators = [DataRequired()])
    choice = StringField('Email:', validators = [DataRequired()])
    help = StringField('Name:', validators = [DataRequired()])
    comment = StringField('Email:', validators = [DataRequired()])


class DetailsView(BaseView):
    @expose("/")
    def index(self):
        if current_user.is_admin == True:
            posts = StudentData.query.order_by(StudentData.timestamp.desc()).all()
            return self.render("admin/details.html", posts = posts)
        else:
            return self.render("404.html")
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            render_template("404.html")
    def inaccessible_callback(self, name, **kwargs):
        if not current_user.is_admin:
            return render_template("404.html")

class BackView(BaseView):
    @expose("/")
    def index(self):
        if  current_user.is_authenticated:
            return self.render("welcome.html")

    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            render_template("404.html")
    def inaccessible_callback(self, name, **kwargs):
        return "not authorized to view this page"

class Controller(ModelView):
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            render_template("404.html")
    def not_auth(self):
        return "not authorized to view this page"

admin.add_view(Controller(Data,db.session))
admin.add_view(Controller(StudentData,db.session))
admin.add_view(DetailsView(name = "Details", endpoint = "detail"))
admin.add_view(BackView(name = "Sign out"))


@login_manager.user_loader
def get_user(ident):
  return Data.query.get(int(ident))


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes = 5)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason = e.description), 400


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/login",methods = ["POST","GET"])
def login():
    form = ReusableForm(request.form)
    if request.method == "POST" and form.validate():
        firstname = request.form["firstname"]
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

                data = Data(firstname, lastname, email, password1, contact, school, classification, major, gender)
                db.session.add(data)
                db.session.commit()
                flash("Documents succesfully submitted. You can now log into your account")
                return render_template("StudentReg.html",form = form, isIndex = True)

            else:
                flash("Email Already in use")
                #render_template("StudentReg.html")
        except DataError:
            flash("Invalid data entry on contact. Enter 10 digits only")
            #render_template("StudentReg.html")
        except db.session.rollback():
            raise
    flash("all fields are required")
    flash("password must match confirm password")
    return render_template("StudentReg.html")


@app.route("/signup")
def signup():
    return render_template("StudentReg.html")


@app.route("/signedin", methods = ["POST","GET"])
@csrf.exempt
def signedin():

    if request.method == "POST":
        email = request.form["studentemail"]
        pword = request.form["studentpassword"]
        chk = True if request.form.get("chk") else False
        hashedpassword = db.session.query(Data.Password).filter(Data.Email == email).scalar()
        user = Data.query.filter_by(Email = email).first()
        if db.session.query(Data).filter(Data.Email == email).count() == 1 and check_password(hashedpassword,pword) == True:
            #session["log"] = True
            login_user(user,remember=chk)
            flash("login success")
            return redirect(url_for("mainpage"))
        flash("Invalid Username or password")
        return render_template("welcome.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("loggout succesfull")
    return redirect(url_for("index"))


@app.route("/confirmation", methods = ["POST","GET"])
def confirmation():
    form = StudentForm(request.form)
    if request.method == "POST" and form.validate():
        preferedname = request.form["pname"]
        email = request.form["email"]
        classes = request.form["textarea1"]
        day = request.form["textarea2"]
        date = request.form["date"]
        time = request.form["time"]
        choice = request.form["choice"]
        areas = request.form["help"]
        comment = request.form["comment"]
        data_id = current_user.id
        stud=StudentData(preferedname, classes, day, date, time, choice, areas, comment, data_id)
        db.session.add(stud)
        db.session.commit()
        #emailing.send_email(preferedname,day,date,time,classes,email)
        t1 = threading.Thread(target=emailing.send_email, args=(preferedname,day,date,time,classes,email))
        t1.start()
        return render_template("confirmStudent.html")
    flash("all fields are required")
    return render_template("mainStudent.html")


@app.route("/delete")
@login_required
def delete():
    if current_user.is_authenticated:
        x = db.session.query(Data).get(current_user.id)
        db.session.delete(x)
        db.session.commit()
        flash("We are sorry to see you go. You can always sign up with us again")
        return redirect(url_for("index"))



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route("/mainpage")
@login_required
def mainpage():
    return render_template("mainStudent.html")


@app.route('/explore')
@login_required
def explore():
    if current_user.is_authenticated:
        page = request.args.get('page', 1 , type = int)
        posts = StudentData.query.order_by(StudentData.timestamp.desc()).paginate(page = page, per_page = 5)
        return render_template('post.html', posts=posts)
    else:
        return render_template("404.html")


@app.route('/confirmed')
@login_required
def confirmed():
    render_template("confirmStudent.html")

@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

@app.after_request
def add_header1(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.after_request
def add_header2(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.after_request
def add_header3(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.after_request
def add_header4(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response
@app.after_request
def add_header5(response):
    response.headers['Expect-CT'] = 'enforce, max-age=43200, report-uri="https://tedtutor.herokuapp.com/report"'
    return response
@app.after_request
def add_header6(response):
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response



@app.route("/question",methods=["POST","GET"])
def question():

    return render_template("questions.html")

@app.route("/posted",methods=["POST","GET"])
@login_required
def posted():
    if request.method == "POST":
        Title = request.form["title"]
        body = request.form["question"]
        user_id = current_user.id
        post = Post(body,Title,user_id = user_id)
        db.session.add(post)
        db.session.commit()
        flash("Your question has posted ")
        return render_template("questions.html")

@app.route('/comment')
@login_required
def comment():
    if current_user.is_authenticated:
        page = request.args.get('page', 1 , type = int)
        posts = Post.query.order_by(Post.timestamp.desc()).paginate(page = page, per_page = 5)
        return render_template('answers.html', posts=posts)
    else:
        return render_template("404.html")

"""@app.before_request
def det():
    print("this is",request.form)
    print("this is", request.headers)"""


if __name__ == '__main__':
    app.run(debug= False)
