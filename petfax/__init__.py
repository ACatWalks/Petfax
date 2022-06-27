from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, Petfax!'
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import show
    app.register_blueprint(show.bp2, url_prefix='/pets/<int:id>')

    from . import form
    app.register_blueprint(form.bp3, url_prefix='/facts/new')
    

    return app