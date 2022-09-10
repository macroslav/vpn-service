from dotenv import load_dotenv
import os

load_dotenv()

SERVER_PUBLIC_KEY = os.environ.get('SERVER_PUBLIC_KEY', '')
ENDPOINT = os.environ.get('ENDPOINT', '')
DNS = os.environ.get('DNS', '')
