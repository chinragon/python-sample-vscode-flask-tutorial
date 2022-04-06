""" 
In this sample, the Flask app object is contained within the hello_app *module*;
that is, hello_app contains an __init__.py along with relative imports. Because
of this structure, a file like webapp.py cannot be run directly as the startup
file through Gunicorn; the result is "Attempted relative import in non-package".

The solution is to provide a simple alternate startup file, like this present
startup.py, that just imports the app object. You can then just specify
startup:app in the Gunicorn command.
"""

from hello_app.webapp import app

<<<<<<< HEAD
print("a")
=======
print("b")
>>>>>>> 13b1d5d0bc634a1b3a4b2ae8060c00efbbb479b6
