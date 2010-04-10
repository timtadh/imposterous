import os
import smtplib
import mimetypes
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

def mail(user, to, subject, text, html, *attachments):
    pswd = getpass.getpass("pass: ")

    msg = MIMEMultipart('related')
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.preamble = 'This is a multi-part message in MIME format.'

    alt = MIMEMultipart('alternative')
    msg.attach(alt)

    msgtext = MIMEText(text)
    alt.attach(msgtext)

    msgtext = MIMEText(html, 'html')
    alt.attach(msgtext)

    for path in attachments:
        msg.attach(make_attach(path))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    login = False
    while not login:
        try:
            mailServer.login(user, pswd)
            login = True
        except smtplib.SMTPAuthenticationError, e:
            print "password rejected", user, pswd, e
            pswd = getpass.getpass("pass: ")
    mailServer.sendmail(user, to, msg.as_string())
    mailServer.close()

    print('Sent email to %s' % to)

def make_attach(path):
    path = os.path.abspath(path)
    contentType, encoding = mimetypes.guess_type(path)

    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'

    main_type, sub_type = contentType.split('/', 1)
    f = open(path, 'rb')
    bytes = f.read()
    f.close()

    if main_type == 'text':
        attachment = MIMEText(bytes)
    elif main_type == 'message':
        attachment = email.message_from_string(bytes)
    elif main_type == 'image':
        attachment = MIMEImage(bytes, sub_type)
        attachment.add_header('Content-ID', ''.join(('<', os.path.basename(path), '>')))
    elif main_type == 'audio':
        print sub_type
        attachment = MIMEAudio(bytes, sub_type)
    else:
        attachment = MIMEBase(main_type, sub_type)
    attachment.set_payload(bytes)
    encode_base64(attachment)

    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
    return attachment

if __name__ == "__main__":
    mail("tim.tadh@gmail.com", "tim.tadh@gmail.com", "hello", "some text", "<h1>some text</h1>")
