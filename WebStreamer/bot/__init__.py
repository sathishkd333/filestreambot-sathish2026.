from pyrogram import Client
# Fixed relative import (assumes vars.py is in the same folder)
from vars import Var 

StreamBot = Client(
    name="Web Streamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS,
    # Optional: plugins=dict(root="plugins") # Automatically loads handlers
)

if __name__ == "__main__":
    print("Bot is starting...")
    StreamBot.run()
