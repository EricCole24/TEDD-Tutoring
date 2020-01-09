"""
DOCSTRING
This function automatically sends individuals
who book tutoring appointments the details of their schedule
"""

from email.mime.text import MIMEText
import smtplib


def send_email(name, day, date, time, classes, email):
    """

    :param day:
    :param date:
    :param time:
    :param name: registered user name
    :param classes: classes needing help with
    :param email: email address for sending information
    :return:
    """

    from_email = "teddtutor@gmail.com"
    from_password = "erichime"
    to_email = email
    subject = "Tutoring Schedule"
    message = "Hey <strong>{}</strong> we appreacte your " \
              "effort in scheduling an appointment for <strong>{} </strong> <strong>{}</strong> " \
              "at <strong>{}</strong> ." \
              "Someone with experience " \
              "in <strong>{}</strong> will be contacting you soon".format(name, day, date, time, classes)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)

    gmail.send_message(msg)
