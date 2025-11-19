class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/flask_rbac_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'