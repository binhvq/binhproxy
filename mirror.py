import webapp2
import urllib2
from google.appengine.api import urlfetch


class MainPage(webapp2.RequestHandler):

    def post(self):
        url = self.request.get("url")
        headers = {"User-Agent": self.request.headers.get("User-Agent")}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        self.response.write(the_page)

app = webapp2.WSGIApplication([
    ('/', MainPage)
])
