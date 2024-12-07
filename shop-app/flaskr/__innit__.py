import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder='templates/website')  # Specify the template folder

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        products = [
            {"name": "Product 1", "price": "$10"},
            {"name": "Product 2", "price": "$20"},
        ]
        return render_template('index.html', products=products)  # 'index.html' is now in 'templates/website'

    return app
