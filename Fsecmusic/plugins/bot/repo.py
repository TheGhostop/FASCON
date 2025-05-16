from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Fsecmusic import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝙁𝘼𝙇𝘾𝙊𝙉 𝙃𝙀𝙍𝙀 ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/xi_xi_xi_xi_xi_xi"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/source_code_network"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/+Y9O5ptuPEFs3NGE1"),          
             InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://github.com/codex-ML/CHOCO-MUSIC-API-BOT"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/cb9394eec3d0ebce858f9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
