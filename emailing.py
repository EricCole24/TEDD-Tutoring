"""
DOCSTRING
emailing users
"""

from email.mime.text import MIMEText
import smtplib


def send_email(name, classes, email):
    """

    :param name: registered user name
    :param classes: classes needing help with
    :param email: email address for sending information
    :return:
    """

    from_email = "info.syst12@gmail.com"
    from_password = ""
    to_email = email
    subject = "Tutoring Schedule"
    message = "Hey <strong>{}</strong> we appreacte your " \
              "effort in booking and appointment." \
              "Someone with experience " \
              "in <strong>{}</strong> will be contacting you soon".format(name, classes)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)

    gmail.send_message(msg)
