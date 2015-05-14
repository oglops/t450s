import smtplib
from email.mime.text import MIMEText
from email.header import Header


# -----------------------------------------------------------
# don't change the following if you don't know what you are doing
# mobile number 15224537411
smtp_server = "smtp.163.com"
mail_user = "t450s_us@163.com"
mail_pwd = "ikvvppfkabwekdyb"
FROM = mail_user


def send_email(notify_email, msg, body='',):
    # TO = ['recepient@mailprovider.com'] #must be a list
    # TO = [notify_email]
    TO = notify_email

    # SUBJECT = "Testing sending using gmail"
    # TEXT = "Testing sending mail using gmail servers"
    SUBJECT = msg
    TEXT = body

    # Prepare actual message
    # message = """\From: %s\nMessage-Id:<20050329231145.62086.mail@mail.emailprovider.com>\nTo: %s\nSubject: %s\n\n%s
    # message = u"""\From: %s\nMessage-Id:<abcdef@mail.com>\nTo: %s\nSubject: %s\n\n%s
    # """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    msg = MIMEText(TEXT, _charset="UTF-8")
    msg['Subject'] = Header(SUBJECT, "utf-8")
    msg['FROM'] = FROM
    msg['To'] = TO

    try:
        #server = smtplib.SMTP(SERVER)
        # or port 465 doesn't seem to work!
        server = smtplib.SMTP(smtp_server, 25)
        # server.ehlo()
        # server.starttls()
        # server.ehlo()
        server.login(mail_user, mail_pwd)
        server.sendmail(FROM, TO, msg.as_string())
        # server.quit()
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print "failed to send mail", e


if __name__ == "__main__":
    send_email('test', 'body')
