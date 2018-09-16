import webapp2
import jinja2
from model import os

jinja_env = jinja2.Environment(
    loader =jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ProjectsPage(webapp2.RequestHandler):
    def post(self):
        projects_template = jinja_env.get_template('BP_projects.html')
        self.response.write(projects_template.render())


app = webapp2.WSGIApplication([
    ('/projects', ProjectsPage),
], config=config,
   debug=True)
