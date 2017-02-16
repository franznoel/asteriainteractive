from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

class Options(ndb.Model):
  name = ndb.StringProperty()
  value = ndb.StringProperty()
  
class Users(ndb.Model):
  username = ndb.StringProperty()
  password = ndb.StringProperty()
  nickname = ndb.StringProperty()
  displayName = ndb.StringProperty()
  status = ndb.StringProperty()
  dateCreated = ndb.DateTimeProperty(auto_now_add=True)
  dateUpdated = ndb.DateTimeProperty(auto_now=True)

class Pages(ndb.Model):
  author = ndb.StringProperty()
  publishDate = ndb.StringProperty()
  content = ndb.TextProperty()
  title = ndb.TextProperty()
  description = ndb.TextProperty()
  excerpt = ndb.TextProperty()
  password = ndb.StringProperty()
  name = ndb.StringProperty()
  menu_order = ndb.IntegerProperty()
  post_type = ndb.StringProperty()
  allow_attachments = ndb.BooleanProperty()
  allow_comments = ndb.BooleanProperty()
  post_mime_type = ndb.StringProperty()
  dateCreated = ndb.DateTimeProperty(auto_now_add=True)
  dateUpdated = ndb.DateTimeProperty(auto_now=True)
  
class Comments(ndb.Model):
  content = ndb.TextProperty()
  author = ndb.StringProperty()
  dateCreated = ndb.DateTimeProperty(auto_now_add=True)
  dateUpdated = ndb.DateTimeProperty(auto_now=True)
  
class Contact(ndb.Model):
  fullname = ndb.StringProperty()
  email = ndb.StringProperty()
  phoneNumber = ndb.StringProperty()
  website = ndb.StringProperty()
  subject = ndb.StringProperty()
  message = ndb.TextProperty()
  created = ndb.DateTimeProperty(auto_now_add=True)
  
class Customers(ndb.Model):
  kind = ndb.StringProperty()
  fullname = ndb.StringProperty()
  customerDomain = ndb.StringProperty()
  phoneNumber = ndb.StringProperty()
  alternateEmail = ndb.StringProperty()
  resourceUiUrl = ndb.StringProperty()
  dateCreated = ndb.DateTimeProperty(auto_now_add=True)
  dateUpdated = ndb.DateTimeProperty(auto_now=True)

class CustomerAddress(ndb.Model):
  kind = ndb.StringProperty()
  contactName = ndb.StringProperty()
  organizationName = ndb.StringProperty()
  locality = ndb.StringProperty()
  region = ndb.StringProperty()
  postalCode = ndb.StringProperty()
  countryCode = ndb.StringProperty()
  addressLine1 = ndb.StringProperty()
  addressLine2 = ndb.StringProperty()
  addressLine3 = ndb.StringProperty()
  dateCreated = ndb.DateTimeProperty(auto_now_add=True)
  dateUpdated = ndb.DateTimeProperty(auto_now=True)
  
  