import webapp2, jinja2, os, sys, model
from google.appengine.api import mail

environment = jinja2.Environment( 
  loader = jinja2.FileSystemLoader( os.path.join( os.path.dirname(__file__),'templates','professional') ), 
  extensions=['jinja2.ext.autoescape'] 
)

class BaseHandler(webapp2.RequestHandler):
  def render_html(self,temp,val=''):
    self.response.content_type = 'text/html'
    try:
      t = environment.get_template(temp)
      self.response.out.write(t.render(val))
    except jinja2.TemplateNotFound:
      t = environment.get_template('error_default.html')
      self.response.out.write(t.render(val))
      
class MainHandler(BaseHandler):
  def get(self):
    val = {'greeting':'Hello World!'}
    self.render_html('index.html',val)
    
class ContactFormHandler(BaseHandler):
  def post(self):
    # Save to Contact
    contact = model.Contact()
    contact.fullname = self.request.get("fullname")
    contact.email = self.request.get("email")
    contact.phoneNumber= self.request.get("phoneNumber")
    contact.website = self.request.get("website")
    contact.subject = self.request.get("subject")
    contact.message = self.request.get("message")
    contact.put()
    
    # Email
    message = mail.EmailMessage(
      sender = self.request.get("fullname") + "<" + self.request.get("email") + ">",
      subject= "AI Contact: "+self.request.get("subject")
    )
    message.to = "Franz Noel Tanglao <franz@asteriainteractive.com>"
    message.body = self.request.get("message")
    message.send()
    #self.redirect("/contact")
    
    
class RegistrationFormHandler(BaseHandler):
  def post(self):
    customer = model.Customers()
    customer.kind = "reseller#customer"
    customer.fullname = self.request.get("contactName")
    customer.customerDomain = self.request.get("customerDomain")
    customer.phoneNumber = self.request.get("phoneNumber")
    customer.alternateEmail = self.request.get("alternateEmail")
    customer.resourceUiUrl = self.request.get("resourceUiUrl")
    customer_key = customer.put()
    customerAddress = model.CustomerAddress(parent=customer_key)
    customerAddress.kind = "customers#address"
    customerAddress.contactName = self.request.get("contactName")
    customerAddress.organizationName = self.request.get("organizationName")
    customerAddress.locality = self.request.get("locality")
    customerAddress.region = self.request.get("region")
    customerAddress.postalCode = self.request.get("postalCode")
    customerAddress.countryCode = "+1"
    customerAddress.addressLine1 = self.request.get("addressLine1")
    customerAddress.addressLine2 = self.request.get("addressLine2")
    customerAddress.addressLine3 = self.request.get("addressLine3")
    customerAddress.put()
    self.redirect("/registration")

class StaticHandler(BaseHandler):
  def get(self, url):
    self.render_html(url+'.html')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/contact/', ContactFormHandler),
    ('/registration/', RegistrationFormHandler),
    ('/(.*?)', StaticHandler),
], debug=False)