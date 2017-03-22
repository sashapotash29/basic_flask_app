from app import db
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime, date




# ALL YOUR MODELS FOR EACH TABLE GOES BELOW
#EXAMPLE


# class User(db.Model):
# 	__tablename__="users"
# 	def __init__(self,username,password,first_name,last_name, creation_date):
# 		self.username = username
# 		self.password = password
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.creation_date = creation_date
		
		

# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(40), unique=True)
# 	password = db.Column(db.String(200))
# 	first_name = db.Column(db.String(40))
# 	last_name = db.Column(db.String(40))
# 	creation_date = db.Column(db.Date, default = date.today())