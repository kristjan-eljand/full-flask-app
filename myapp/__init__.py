import os

from flask import Flask

def create_app(test_config=None):
    """Our application factory
    
    """
    #=============================
    # create and configure the app
    #=============================
    # __name__ tells the app where it is located
    # instance_relative_config tells that configuration files are relative to instance folder
    # the instance folder is located outside myapp folder and holds data like configuration secrets and database file
    app = Flask(__name__, instance_relative_config=True)
    
    #=============================
    # set default configuration
    #=============================
    # SECRET_KEY is dev to enable convenient development but should be overridden when deploying
    # DATABASE is the path where the SQLite database file will be saved.
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Database is out of scope for now
        #DATABASE=os.path.join(app.instance_path, 'myapp.sqlite'),
    )

    #============================
    # override default configuration
    #============================
    # app.config.from_pyfile takes values from config.py that is in instance folder
    # and overrides the default configuration. This can be used to set the real SECRET_KEY
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # instance folder needs to be created if it doesn't exist
    # to have a place to put database file
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #==============================
    # auth0 logic
    #==============================

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    return app