
import asyncio
from pyrogram import Client, idle
from ..vars import Var

StreamBot = Client(
    name="Web Streamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

async def main():
    await StreamBot.start()
    print("Bot started successfully!")
    await idle() # Keeps the script running until interrupted
    await StreamBot.stop()

if __name__ == "__main__":
    asyncio.run(main())
