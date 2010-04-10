import sendmail
import markdown

sub = raw_input("subject: ")
text = open(raw_input("file: "), "r").read()

attach = raw_input("attachments? ")[0].lower()
attachments = list()
while attach == 'y':
    attachments.append(raw_input("path: "))
    attach = raw_input("another? ")[0].lower()

print "attachments", attachments

sendmail.mail("tim.tadh", "tim.tadh@gmail.com", sub, text,
              markdown.markdown(text).replace('<br>', ''), *attachments)
