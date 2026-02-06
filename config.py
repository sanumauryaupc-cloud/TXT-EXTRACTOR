import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "38528250"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "2ed087f9139515b3fd05d63072f56672")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7803387854:AAFTcsui4jvkWdhWIYNtB2B2dZGegSTyO8g")

OWNER_ID = int(os.environ.get("OWNER_ID", "7803387854"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
