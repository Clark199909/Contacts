from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:20176098wd@localhost/contacts'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/courses'
>>>>>>> 1513e7d8644864ca1507324ae9fd9f013fa804f4
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)
