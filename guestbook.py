import sys
import os
import logging
import webapp2

# Setup the import path
package_dir = "controllers"
package_dir_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), package_dir))
if not package_dir_path in sys.path:
	sys.path.insert(0, package_dir_path)

from controllers import MainPage
from controllers import Guestbook

application = webapp2.WSGIApplication([
    ('/', MainPage.MainPage),
    ('/sign', Guestbook.Guestbook),
], debug=True)

# Extra Hanlder like 404 500 etc
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Oops! we are not here, leave a message ... (This is a 404)')
    response.set_status(404)

application.error_handlers[404] = handle_404