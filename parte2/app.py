from flask import Flask
from database import init_db
from controller import userController

app = Flask(__name__)

init_db(app)
app.register_blueprint(userController)

if __name__ == "__main__":
    app.run()

# __init__.py é uma boa forma para ser utilizado no mvc, além de ajudar a evitar erros =)