import os

from dotenv import load_dotenv

load_dotenv('.env')

TOKEN = os.getenv('USTOZ_SHOGIRT')
ADMIN = os.getenv('ADMIN')
