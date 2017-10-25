from flask import Flask,  url_for
app = Flask(__name__, static_url_path = '', static_folder = 'static', template_folder = 'templates')

app.config['DEBUG'] = True
TEMPLATES_AUTO_RELOAD = True
