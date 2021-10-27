import os

from pathlib import Path  # python3 only
from dotenv import load_dotenv
from dotenv.main import find_dotenv
#load_dotenv(find_dotenv()) #this line only finds .env but doesnt find .flaskenv

env_path1 = Path('/Users/AhmetKideys/Desktop/Programming/GitHub/FlaskPolitoGithubFolder/.flaskenv') 
load_dotenv(dotenv_path=env_path1)

env_path2 = Path('/Users/AhmetKideys/Desktop/Programming/GitHub/FlaskPolitoGithubFolder/.env') 
load_dotenv(dotenv_path=env_path2)

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')



