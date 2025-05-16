import requests
import aiofiles
import aiohttp
import asyncio
import os
import uuid
import base64
import mimetypes
import shutil
from re import findall
from pyrogram import Client, filters
from pyrogram.enums import ChatAction, ParseMode, MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from MukeshAPI import api
from lexica.constants import languageModels
from httpx import AsyncClient
from Fsecmusic import app


@app.on_message(filters.command(["alcon"], prefixes=["F", "f"]))
async def chat_gpt(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        
        name = message.from_user.first_name if message.from_user else "User"
        
        if len(message.command) < 2:
            await message.reply_text(f"Hello {name}, how can I help you today?")
        else:
            query = message.text.split(' ', 1)[1]
            response = api.gemini(query)["results"]
            await message.reply_text(f"{response}", parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"Error: {e}")
