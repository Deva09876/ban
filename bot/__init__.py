import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)   

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)


@bot.on_message(filters.command("banall"))
async def _(bot, msg):
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)

@bot.on_message(filters.command("start"))
async def start(bot, msg):
    await message.reply(text="On")

