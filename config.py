class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "/home/kanak/environments/Flask_Application/flask_application/static/img"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAXIMUM_CONTENT_LENGTH = 50*1024*1024

    
    CLIENT_IMAGES="/home/kanak/environments/Flask_Application/flask_application/static/client/img"
    CLIENT_CSV="/home/kanak/environments/Flask_Application/flask_application/static/client/csv"
    CLIENT_PDF="/home/kanak/environments/Flask_Application/flask_application/static/client/pdf"


    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "Users"
    DB_USERNAME = "root"
    DB_PASSWORD = "kanak@16"

    IMAGE_UPLOADS = "/home/kanak/environments/Flask_Application/flask_application/static/img"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAXIMUM_CONTENT_LENGTH = 50*1024*1024

    CLIENT_IMAGES="/home/kanak/environments/Flask_Application/flask_application/static/client/img"
    CLIENT_CSV="/home/kanak/environments/Flask_Application/flask_application/static/client/csv"
    CLIENT_PDF="/home/kanak/environments/Flask_Application/flask_application/static/client/pdf"

    SECRET_KEY='gsiWHlrVMgBv4alAjlukKw'
    SESSION_COOKIE_SECURE = False
