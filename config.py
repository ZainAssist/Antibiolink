import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv()

# Try to get from environment variables (Heroku Config Vars)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH") 
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# If env vars are not set, try to load from env_config.json
if not all([API_ID, API_HASH, BOT_TOKEN, MONGO_URI]):
    try:
        with open("env_config.json", "r") as f:
            config = json.load(f)
            API_ID = API_ID or config.get("API_ID")
            API_HASH = API_HASH or config.get("API_HASH")
            BOT_TOKEN = BOT_TOKEN or config.get("BOT_TOKEN")
            MONGO_URI = MONGO_URI or config.get("MONGO_URI")
    except FileNotFoundError:
        pass

# Bot Owner Configuration - Add your user ID and username here
BOT_OWNER = os.getenv("OWNER_ID")
BOT_OWNER_USERNAME = os.getenv("OWNER_USERNAME")

# If env vars are not set, try to load from env_config.json
if not BOT_OWNER or not BOT_OWNER_USERNAME:
    try:
        with open("env_config.json", "r") as f:
            config = json.load(f)
            if not BOT_OWNER:
                BOT_OWNER = config.get("OWNER_ID")
            if not BOT_OWNER_USERNAME:
                BOT_OWNER_USERNAME = config.get("OWNER_USERNAME")
    except FileNotFoundError:
        pass

# Convert to int if it's a string
if BOT_OWNER:
    BOT_OWNER = int(BOT_OWNER)


DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute"  # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*'
)

# Image URLs for command responses
# Use more reliable URLs or set to None to use text-only fallback
START_IMG_URL = os.getenv("START_IMG_URL", "https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg")  # Default bot icon
HELP_IMG_URL = os.getenv("HELP_IMG_URL", "https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg")  # Default help icon
CONFIG_IMG_URL = os.getenv("CONFIG_IMG_URL", "https://graph.org/file/272610985cc3a83a93c12-f258d6104db16b53e3.jpg")  # Default settings icon

# Owner username - for owner button (add @ symbol if needed)
BOT_OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Uff_Zainu")
