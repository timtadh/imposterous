import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64

def mail(to, subject, text, *attachments):
    user = 'tim.tadh@gmail.com'
    pswd = raw_input("pass: ")

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for path in attachments:
        msg.attach(make_attach(path))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, pswd)
    mailServer.sendmail(user, to, msg.as_string())
    mailServer.close()

    print('Sent email to %s' % recipient)

def make_attach(path):
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
    elif main_type == 'audio':
        print sub_type
        attachment = MIMEAudio(bytes, sub_type)
    else:
        attachment = MIMEBase(main_type, sub_type)
    attachment.set_payload(bytes)
    encode_base64(attachment)

    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
    return attachment

mail("tim.tadh@gmail.com", "hello", "some text", "/home/hendersont/Desktop/Regex_Tim_Henderson_3-31-2010.mp3")