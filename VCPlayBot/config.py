import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "XD_CUTETY")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/3a31846c10923f06ca62e.mp4")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SONA_OP00")
OWNER_NAME = getenv("OWNER_NAME", "ID_SELLER00")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Y_K_D_1")
PROJECT_NAME = getenv("PROJECT_NAME", "Sona")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/CuteBaccha/Sonamusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5096741943").split()))
