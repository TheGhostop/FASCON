
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from Fsecmusic import app
from Fsecmusic.core.call import FALCON
from Fsecmusic.utils import bot_sys_stats
from Fsecmusic.utils.decorators.language import language
from Fsecmusic.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://telegra.ph/file/7653a76ce689b59765c2a.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await FALCON.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
