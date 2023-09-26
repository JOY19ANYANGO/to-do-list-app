from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class TableToDo(db.Model):
    __tablename__ = 'table_to_do'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
   
