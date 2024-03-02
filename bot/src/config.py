from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BACK_URL = os.environ.get('BACK_URL')
ADMIN_ID = os.environ.get('ADMIN_ID')
# 5900962019 