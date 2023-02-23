from werkzeug.security import generate_password_hash
from . import db
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Product, Img, Color, ConfigProd, User



main = Blueprint('main', __name__)
# @main.before_request
# def do_something_only_once():
#     # admin
#     admin = User(name="admin", email="admin@mail.com", is_admin=True, password=generate_password_hash("admin", method='sha256'))

#     #1 product
#     product1 = Product(nameProd = 'Beats EP', description = 'The preferred choice of a vast range of acclaimed DJs. Punchy, bass-focused sound and high isolation. Sturdy headband and on-ear cushions suitable for live performance', price = 100, category = 'Headphones', img_prev = 'black.png' )
    
#     imgBlack1 = Img(img='black.png', product=product1)
#     imgBlue2 = Img(img='blue.png', product_id=1)
#     imgRed3 = Img(img='red.png', product_id=1)

#     colorBlack1 = Color(name='black', img=imgBlack1, product=product1)
#     colorBlue2 = Color(name = 'blue', img=imgBlue2,  product_id=1)
#     colorRed3 = Color(name='red', img=imgRed3, product_id=1)

#     confStraight1 = ConfigProd(name = 'Sraight', product=product1)
#     confCoiled2 = ConfigProd(name = 'Coiled', product_id=1)
#     confLong3 = ConfigProd(name = 'Long-coiled', product_id=1)

#     db.drop_all()
#     db.create_all()

#     db.session.add(product1)
#     db.session.add_all([imgBlack1, imgBlue2, imgRed3])
#     db.session.add_all([colorBlack1, colorBlue2, colorRed3])
#     db.session.add_all([confStraight1, confCoiled2, confLong3])

    
#     db.session.add(admin)
#     db.session.commit()


@main.route('/', methods=['GET', 'POST'])
def index():
        # admin

        #1 product
        # product1 = Product(nameProd = 'Beats EP', description = 'The preferred choice of a vast range of acclaimed DJs. Punchy, bass-focused sound and high isolation. Sturdy headband and on-ear cushions suitable for live performance', price = 100, category = 'Headphones', img_prev = 'black.png' )
    
        # imgBlack1 = Img(img='black.png', product=product1)
        # imgBlue2 = Img(img='blue.png', product_id=1)
        # imgRed3 = Img(img='red.png', product_id=1)

        # colorBlack1 = Color(name='black', img=imgBlack1, product=product1)
        # colorBlue2 = Color(name = 'blue', img=imgBlue2,  product_id=1)
        # colorRed3 = Color(name='red', img=imgRed3, product_id=1)

        # confStraight1 = ConfigProd(name = 'Sraight', product=product1)
        # confCoiled2 = ConfigProd(name = 'Coiled', product_id=1)
        # confLong3 = ConfigProd(name = 'Long-coiled', product_id=1)

    #2 product
    # product2 = Product(nameProd = 'Beats E++', description = 'The preferred choice of a vast range of acclaimed DJs. Punchy, bass-focused sound and high isolation. Sturdy headband and on-ear cushions suitable for live performance', price = 200, category = 'Headphones', img_prev = '2red.png' )
    
    # img2Black1 = Img(img='2black.png', product=product2)
    # img2Blue2 = Img(img='2blue.png', product_id=2)
    # img2Red3 = Img(img='2red.png', product_id=2)

    # color2Black1 = Color(name='black', img=img2Black1, product=product2)
    # color2Blue2 = Color(name = 'blue', img=img2Blue2,  product_id=2)
    # color2Red3 = Color(name='red', img=img2Red3, product_id=2)

    # conf2Straight1 = ConfigProd(name = 'Sraight', product=product2)
    # conf2Coiled2 = ConfigProd(name = 'Coiled', product_id=2)
    # conf2Long3 = ConfigProd(name = 'Long-coiled', product_id=2)


        
    #     db.session.add(product1)
    # # db.session.add_all([img2Black1, img2Blue2, img2Red3])
    # # db.session.add_all([color2Black1, color2Blue2, color2Red3])
    # # db.session.add_all([conf2Straight1, conf2Coiled2, conf2Long3])
    # # db.session.commit()
    # # db.session.add(product2)
    #     db.session.add_all([imgBlack1, imgBlue2, imgRed3])
    #     db.session.add_all([colorBlack1, colorBlue2, colorRed3])
    #     db.session.add_all([confStraight1, confCoiled2, confLong3])

    #     db.session.commit()





    products = Product.query.all()
    #imgs = db.session.query(Img.product_id).distinct().all()
    #imgs = select(Img).where(Img.product_id.in_(["spongebob", "sandy"]))


    if request.method == 'POST':
        if request.form['submit_button'] == 'Grid':
            return render_template('index.html', button=1, products=products)
        elif request.form['submit_button'] == 'Table':
            return render_template('index.html', button=0, products=products)

    return render_template('index.html', button = 1, products=products)



@main.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@main.route('/product/<int:product_id>/', methods=['GET', 'POST'])
def product(product_id):
    product = Product.query.get_or_404(product_id)
    image = Img.query.filter_by(product_id=product_id).all()
    return render_template('product.html', product=product, image=image)

