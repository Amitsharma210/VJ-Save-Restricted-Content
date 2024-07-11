import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26406803"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bee8853d1219e889f6ce5452dc9ef842")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://towripweb:q3eKL0mBKgIzOhaE@mongodburl.xngfwsj.mongodb.net/?retryWrites=true&w=majority&appName=Mongodburl")
