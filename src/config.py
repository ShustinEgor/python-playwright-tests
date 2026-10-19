import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://dummyjson.com")

BASE_URL_UI= os.getenv("BASE_URL_UI", "https://www.saucedemo.com/")
USERNAME_UI= os.environ["USERNAME_UI"]
PASSWORD_UI= os.environ["PASSWORD_UI"]