from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User



profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def page():
    return render_template('profile.html', user=current_user)

@profile.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get(id)
    if not user:
        flash('Please sign in')
        return redirect(url_for('auth.login')) 
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user.name = name
        user.email = email
        user.password = generate_password_hash(password, method='sha256')
        db.session.merge(user)
        db.session.commit()
        return redirect(url_for('profile.page'))
    return render_template('editUser.html', user=user)

@profile.route('/deleteUser/<int:id>', methods=['GET', 'POST'])
def deleteUser(id):
    user = User.query.get(id)
    if not user:
        flash('Please sign in')
        return redirect(url_for('auth.login')) 
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.signup')) 