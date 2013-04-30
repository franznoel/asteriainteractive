import webapp2, jinja2, os, re, cgi, hmac, random, string
from models import Account, Job, Resume
from google.appengine.api import mail
from google.appengine.ext import db

environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))
config = {}
config['webapp2_extras.sessions'] = {
  'secret_key': '(spg@j&v76ddh)bq6xcs0di&3uevqh(*_7tnt04!r(yw3+pqn5'
}

class IndexHandler(webapp2.RequestHandler):
  def get(self):
    val = {'greeting':'Hello World!'}
    template = environment.get_template('index.html')
    self.response.out.write(template.render(val))
    

class AccountHandler(webapp2.RequestHandler):
  def get(self):
    self.redirect("/")
    
  def post(self):
    ## Get account request information
    fullname= cgi.escape(self.request.get('fullname'))
    username= cgi.escape(self.request.get('username'))
    email = cgi.escape(self.request.get('email'))
    password = self.hash_password(self.request.get('username'),self.request.get('password'))
    self.send_confirmation_email(email, fullname)
    self.save_info(username, fullname, email, password)
    self.redirect("/")
    
  def save_info(self,username,fullname,email,password):
    account= Account(
      key_name=username,
      fullname=fullname,
      username= username,
      email = email,
      password = password,
    )
    account.put()
    
  def send_confirmation_email(self,email,fullname): # Send Email
    mail.send_mail(
      sender="Asteria Interactive <franz@asteriainteractive.com>", 
      to=fullname+" <"+email+">",
      subject="Confirm Your Asteria Account",
      body="Hi "+fullname+",\n\nWelcome to Asteria Interactive!\n\nClick on the link below to confirm your email address.\n\nThanks!\nAsteria Interactive"
    )
    
  def hash_password(self,username,password):
    salt = ''.join(random.sample(string.letters,5))
    secret = config['webapp2_extras.sessions']['secret_key']
    hashed = hmac.new(secret,username+password+salt).hexdigest()
    hashed_password = '%s|%s' % (hashed,salt)
    return hashed_password
    
    
class JobHandler(webapp2.RequestHandler):
  def get(self):
    self.redirect("/")

  def post(self):
    skills = [x.strip() for x in self.request.get('skills').split(',')]
    job = Job(
      # create the key_name, and parent
      title = self.request.get('title'),
      description = self.request.get('description'),
      address = self.request.get('address'),
      skillsets = skills,
      phone = self.request.get('phone'),
      link = self.request.get('link'),
      isPublic = self.request.get('isPublic'),
    )
    job.put()
    self.redirect("/")


class ResumeHandler(webapp2.RequestHandler):
  def get(self):
    self.redirect("/")
    
  def post(self):
    skills = [x.strip() for x in self.request.get('skills').split(',')]
    resume = Resume(
      # create the key_name, and parent
      title = self.request.get('title'),
      description = self.request.get('description'),
      address = self.request.get('address'),
      skillsets = skills,
      link = self.request.get('link'),
      isPublic = self.request.get('isPublic'),
    )
    resume.put()
    self.redirect('/')
    
class LoginHandler(webapp2.RequestHandler):
  def post(self):
    username = self.request.get('username')
    password = self.request.get('password')
    if self.valid_password(username,password):
      users = db.GqlQuery("""SELECT * FROM Account WHERE username=:1""",username)
      for user in users.run():
        self.response.set_cookie('username',user.fullname,max_age=360,path='/')
        self.response.set_cookie('message','',max_age=360,path='/')
    else:
      self.response.set_cookie('message','Login failed!',max_age=360,path='/')
    self.redirect('/')
    
  def valid_password(self,username,password):
    users = db.GqlQuery("""SELECT * FROM Account WHERE username=:1""",username)
    for user in users.run():
      if user:
        # get salt, get secret, hash new password, and compare 2 hashed passwords
        hashed = user.password.split("|")
        salt = hashed[1]
        current_hashed_password = hashed[0]
        secret = config['webapp2_extras.sessions']['secret_key']
        hashed_password = hmac.new(secret,username+password+salt).hexdigest()
        if hashed_password==current_hashed_password:
          return True
        else:
          return False
  
    
app = webapp2.WSGIApplication([
  ('/', IndexHandler),
  ('/account/', AccountHandler),
  ('/job/', JobHandler),
  ('/login/', LoginHandler),
  ('/resume/', ResumeHandler),
], debug=True)
