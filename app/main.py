import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from pathlib import Path

basedir = Path(__file__).resolve().parent
load_dotenv(find_dotenv())

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    return app
    
if '__main__' == __name__:
    app = create_app()
    
    app.run(port=5000)
