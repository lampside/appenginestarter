import os
import webapp2
import jinja2
import cgi
from google.appengine.api import mail

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "html")))
	
class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template("index.html")
		self.response.out.write(template.render())
		
class ContactHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template("contact.html")
		self.response.out.write(template.render())
		
	def post(self):
		fullname = cgi.escape(self.request.get("fullname"))
		sender = cgi.escape(self.request.get("email"))
		subject = cgi.escape(self.request.get("subject"))
		message = cgi.escape(self.request.get("message"))
		email = "Sender: " + sender + "\n" + "Full name: " + fullname + "\n" + "Message: " + "\n" + message
		
		To = "CLIENT_EMAIL"
		From = "ADMIN_EMAIL"
		mail.send_mail(From, To, subject, email)