

import sys
import os
import logging
import webapp2

# Setup the import path
package_dir = "controllers"
package_dir_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), package_dir))

# Allow unzipped packages to be imported
# from packages folder
if not package_dir_path in sys.path:
	logging.info(sys.path)
	sys.path.insert(0, package_dir_path)
	logging.info("Inserting controllers in path")
logging.info(sys.path)

if not package_dir_path in sys.path:
	logging.info("insert failed")
logging.info("insert succeeded")
# Append zip archives to path for zipimport
# for filename in os.listdir(package_dir_path):
#     if filename.endswith((".zip", ".egg")):
#         path = "%s/%s" % (package_dir_path, filename)
#         if not path in sys.path:
#             logging.debug('Adding zip package %s to path' % path)
#             sys.path.insert(0, path)

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