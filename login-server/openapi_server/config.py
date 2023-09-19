PATH_PULIC_KEY = "public_key.pem"
PATH_SECRETE_KEY = "secret_key.pem"
class Config:
    with open(PATH_PULIC_KEY, "rb") as f:
        JWT_PUBLIC_KEY = f.read()
    with open(PATH_SECRETE_KEY, "rb") as f:
        JWT_PRIVATE_KEY = f.read()
    JWT_ALGORITHM = "RS256"
    SECRET_KEY = "my_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///login.db"
    