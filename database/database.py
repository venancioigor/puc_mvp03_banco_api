from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema
from datetime import date, datetime

db = SQLAlchemy()
ma = Marshmallow()

# CTRL + M + R --- cria region
# region Banco

class BancoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
   
    def __repr__(self):
        return f'<BancoModel {self.id}>'

# Definir o esquema de serialização
class BancoSchema(SQLAlchemySchema):
    class Meta:
        model = BancoModel

    id = ma.auto_field()
    nome = ma.auto_field()
# endregion


