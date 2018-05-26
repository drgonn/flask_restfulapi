from datetime import datetime  #记录时间
import hashlib #加密
from werkzeug.security import generate_password_hash, check_password_hash  #加密密码
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  #生成令牌，暂时不用
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
# from app.exceptions import ValidationError  错误处理
from . import db, login_manager


class Permission:
    CARD_STATUS_QUERY = 1
    POOLS_QUERY = 2

    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0





class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    account = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    confirmed = db.Column(db.Boolean, default=False)   #加以确认

    company = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    phone = db.Column(db.String(64), unique=True)
    location = db.Column(db.String(64))
    about = db.Column(db.Text())


    login_logs = db.relationship('Login_log', backref='user', lazy='dynamic')


class Login_log(db.Model):
    __tablename__ = 'login_logs'
    id = db.Column(db.Integer, primary_key=True)
    login_time = db.Column(db.DateTime(), default=datetime.utcnow)
    action = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Card(db.Model):
    pass