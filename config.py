#-*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or "hard to guess string."
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX='[FLASKY]'
	FLASKY_MAIL_SENDER = '123389602@qq.com'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	FLASKY_POSTS_PER_PAGE=os.environ.get('FLASKY_POSTS_PER_PAGE') or 20
	FLASKY_FOLLOWERS_PER_PAGE=os.environ.get('FLASKY_FOLLOWERS_PER_PAGE') or 10
	FLASKY_FOLLOWED_PER_PAGE = os.environ.get('FLASKY_FOLLOWED_PER_PAGE') or 10
	SQLALCHEMY_RECODE_QUERIES = True
	FLASKY_DB_QUERY_TIMEOUT = 0.5

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG= True
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLE = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
	'developmen':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	
	'default':DevelopmentConfig
	}