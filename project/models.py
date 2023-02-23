from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    is_admin = db.Column(db.Boolean(), default=False)

    def __repr__(self):
      return 'User(email=%s, password=%s, name=%s )' % (self.email, self.password, self.name)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True) 
  img_prev = db.Column(db.String(1000))
  img = db.relationship('Img', backref='product')
  nameProd = db.Column(db.String(1000))
  description = db.Column(db.String(1000))
  price = db.Column(db.Float)
  category = db.Column(db.String(100))
  color = db.relationship('Color', backref='product')
  configProd = db.relationship('ConfigProd', backref='product')

  def __repr__(self):
    return 'Product(nameProd=%s, description=%s, category=%s, img_prev=%s )' % (self.nameProd, self.description, self.category, self.img_prev)


class Img(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  img = db.Column(db.String(1000))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  color = db.relationship('Color', backref='img')
  

  def __repr__(self):
    return 'Img(img=%s)' % (self.img)

class Color(db.Model):
  id =  db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  img_id = db.Column(db.Integer, db.ForeignKey('img.id'))
  def __repr__(self):
    return 'Color(name=%s)' % (self.name)
  
class ConfigProd(db.Model):
  id =  db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  def __repr__(self):
    return 'Color(name=%s)' % (self.name)
