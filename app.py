from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from database.database import  db, ma
from config.swagger import template, swagger_config
from routes.banco_route import bancos

app = Flask(__name__)
port = 5000
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Adicionar o bloco "definitions" no Swagger
app.config['SWAGGER'] = {
    'title': 'Banco - API',
    'uiversion': 3
            }

swagger = Swagger(app, template=template, config=swagger_config)

db.app=app
db.init_app(app)
ma.init_app(app)

# Registrando endpoints
app.register_blueprint(bancos)


# Executar o aplicativo Flask
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host="0.0.0.0", port=port)

