class Config:

    SECRET_KEY = 'ricardomussett'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):

    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/python_test"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ricardomussett@gmail.com'
    MAIL_PASSWORD = '3527354kbx'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'ricardomussett@gmail.com'
    FLASKY_ADMIN = 'FLASKY_ADMIN'


config = {
    'development': DevelopmentConfig
}