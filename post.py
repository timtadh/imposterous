import sendmail
import markdown

sendmail.mail("post@posterous.com", raw_input("subject: "), markdown.markdownFromFile(raw_input("file: ")))
