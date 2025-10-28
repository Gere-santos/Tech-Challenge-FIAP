
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bcrypt_context  = CryptContext(schemes=["bcrypt"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl = "/api/v1/login_form")


from api.routes import router_books


app.include_router(router_books)
