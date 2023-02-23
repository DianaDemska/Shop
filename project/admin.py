from flask import Blueprint, redirect, render_template, url_for, request, get_flashed_messages, flash, abort
import uuid, os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Product, Img, Color, ConfigProd, User
from . import db

admin = Blueprint('admin', __name__)

UPLOAD_FOLDER = 'project/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def adminPage():
    return render_template('adminProfile.html', user=current_user)

@admin.route('/admin/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nameProd = request.form.get('nameProd')
        description = request.form.get('description')
        price = request.form.get('price')
        category = request.form.get('category')
        conf = request.form.getlist('conf')
  

        picture = request.files['picture0']
        color = request.form.get('color0')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))
        img_prev = filename
            
        
        productMain = Product(nameProd=nameProd, description=description, price=price, category=category, img_prev=img_prev )
        img1 = Img(img=filename, product=productMain)
        color1 = Color(name=color, img=img1, product=productMain)
        db.session.add(productMain)
        db.session.add(img1)
        db.session.add(color1)
        db.session.commit()
        last = Product.query.order_by(-Product.id).first()

        picture = request.files['picture1']
        color = request.form.get('color1')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))

        img = Img(img=filename, product_id=last.id)
        color = Color(name = color, img=img,  product_id=last.id)
        db.session.add(img)
        db.session.add(color)
        db.session.commit()

        picture = request.files['picture2']
        color = request.form.get('color2')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))

        img = Img(img=filename, product_id=last.id)
        color = Color(name = color, img=img,  product_id=last.id)
        db.session.add(img)
        db.session.add(color)
        db.session.commit()

        for i in range(len(conf)):
            if i == 0:
                configuration1 = ConfigProd(name = conf[i], product=productMain)
                db.session.add(configuration1)
                db.session.commit()
            else:
                configuration = ConfigProd(name = conf[i], product=last)
                db.session.add(configuration)
                db.session.commit()


        
        return redirect(url_for('admin.adminPage'))
    return render_template('productCreate.html')

@admin.route('/admin/view', methods=['GET', 'POST'])
@login_required
def view():
    products = Product.query.all()
    return render_template('productView.html', products=products)

@admin.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    product = Product.query.get_or_404(id)
    if not product:
        flash('Product not found')
        return redirect(url_for('admin.view')) 
    
    if request.method == 'POST':
        nameProd = request.form.get('nameProd')
        description = request.form.get('description')
        price = request.form.get('price')
        category = request.form.get('category')
        conf = request.form.getlist('conf')

        product.nameProd = nameProd
        product.description = description
        product.price = price
        product.category = category

        picture = request.files['picture0']
        color = request.form.get('color0')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))
        img_prev = filename
        product.img_prev = img_prev    
        
       
        img1 = Img(img=filename, product_id=id)
        color1 = Color(name=color, img=img1, product_id=id)
        db.session.merge(product)
        db.session.merge(img1)
        db.session.merge(color1)
        db.session.commit()

        picture = request.files['picture1']
        color = request.form.get('color1')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))

        img = Img(img=filename, product_id=id)
        color = Color(name = color, img=img,  product_id=id)
        db.session.merge(img)
        db.session.merge(color)
        db.session.commit()

        picture = request.files['picture2']
        color = request.form.get('color2')
        nazwa = uuid.uuid1()
        _, rozszerzenie = os.path.splitext(picture.filename)
        filename = str(nazwa) + rozszerzenie
        picture.save(os.path.join(UPLOAD_FOLDER, filename))

        img = Img(img=filename, product_id=id)
        color = Color(name = color, img=img,  product_id=id)
        db.session.merge(img)
        db.session.merge(color)
        db.session.commit()

        for i in range(len(conf)):
                configuration = ConfigProd(name = conf[i], product_id=id)
                db.session.merge(configuration)
                db.session.commit()

        return redirect(url_for('admin.view'))
    return render_template('productEdit.html', product=product)

@admin.route('/delete/<int:id>')
def delete(id):
    w = Product.query.get(id)
    if w is None:
        abort(404)
    try:
        db.session.delete(w)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('admin.view'))