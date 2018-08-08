# coding: utf-8
from flask import render_template, redirect, request, url_for, flash, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask import jsonify
import request, json


@auth.route('/todo/api/v1.0/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if  user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    status = {'state': 'logout ok'}
    return jsonify(status)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

# 测试直接获取请求，并将请求的内容以json的格式返回
@auth.route('/test1/', methods=["GET", "POST"])
def test1():
    
    print("name:")
    print(request.args.get("name"))
    print("all:")
    print(json.dumps(request.args))
    return json.dumps(request.args)

# 测试蓝本和url是否正常工作
@auth.route('/hello/', methods=['POST', 'GET'])
def hello():
    return jsonify({'username': 'user.username'})
