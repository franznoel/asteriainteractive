from google.appengine.ext import db

class Account(db.Model):
  fullname = db.StringProperty()
  email = db.StringProperty()
  username = db.StringProperty()
  password = db.StringProperty()
  confirmed = db.BooleanProperty()
  
  
class Job(db.Model):
  title = db.StringProperty()
  description = db.TextProperty()
  skillsets = db.StringListProperty()
  address = db.PostalAddressProperty()
  phone = db.PhoneNumberProperty()
  link = db.TextProperty()
  expiration = db.DateTimeProperty()
  isPublic = db.StringProperty()
  

class Resume(db.Model):
  title = db.StringProperty()
  description = db.TextProperty()
  address = db.PostalAddressProperty()
  skills = db.StringListProperty()
  link = db.TextProperty()
  isPublic = db.StringProperty()
