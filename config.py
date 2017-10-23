import os

from setup import basedir

class BaseConfig(object):
	SECRET_KEY = "lolol"
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(object):
	#dev config
	TESTING = True
	DEBUG = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = #later
	DEBUG_TB_ENABLED = True
	PRESERVE_CONTEXT_ON_EXCEPTION = False