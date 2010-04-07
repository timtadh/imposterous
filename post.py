import sendmail
import markdown

sub = raw_input("subject: ")
text = open(raw_input("file: "), "r").read()

sendmail.mail("post@posterous.com", sub, text, markdown.markdown(text).replace('<br>', ''))
