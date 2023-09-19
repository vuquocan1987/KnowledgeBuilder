PATH_PULIC_KEY = "public_key.pem"
PATH_SECRETE_KEY = "secret_key.pem"
class Config:
    SECRET_KEY = "my_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///browsing.db"
    with open("public_key.pem","r") as f:
        JWT_PUBLIC_KEY = f.read()
    
    