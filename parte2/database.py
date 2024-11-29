from flask_sqlalchemy import SQLAlchemy
 
# Objeto da classe
db = SQLAlchemy()

def init_db(app):

    # Configurando a database :)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///first.db"

   

    with app.app_context():
        db.init_app(app)
        db.create_all()