import time
from urllib.parse import urlparse
import os
import asyncio
import requests
import yt_dlp
import wget
from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from Fsecmusic import app

# Constants
MAX_FILESIZE = 50 * 1024 * 1024  # 50MB limit
TEMP_DIR = "downloads"  # Temporary directory for downloads

# Ensure temp directory exists
os.makedirs(TEMP_DIR, exist_ok=True)

@app.on_message(filters.command("audio"))
async def download_song(_, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ sᴏɴɢ ɴᴀᴍᴇ**")
        return

    m = await message.reply("**🔄 sᴇᴀʀᴄʜɪɴɢ...**")
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            await m.edit("**⚠️ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ**")
            return

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = os.path.join(TEMP_DIR, f"{title}.jpg")
        duration = results[0]["duration"]
        views = results[0]["views"]
        channel_name = results[0]["channel"]

        # Download thumbnail
        thumb = requests.get(thumbnail, allow_redirects=True)
        with open(thumb_name, "wb") as f:
            f.write(thumb.content)

        # Configure yt-dlp options
        ydl_opts = {
            "format": "bestaudio[ext=m4a]",
            "outtmpl": os.path.join(TEMP_DIR, "%(title)s.%(ext)s"),
            "quiet": True,
        }

        await m.edit("**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
        
        # Extract info first to check file size
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            if info_dict.get('filesize') and info_dict['filesize'] > MAX_FILESIZE:
                await m.edit("**⚠️ ғɪʟᴇ sɪᴢᴇ ᴛᴏᴏ ʟᴀʀɢᴇ (>50MB)**")
                return

            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        # Calculate duration in seconds
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60

        await m.edit("**📤 ᴜᴘʟᴏᴀᴅɪɴɢ...**")
        
        # Send audio file
        await message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"**🎵 ᴛɪᴛʟᴇ:** {title}\n**👤 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {message.from_user.mention}\n**👀 ᴠɪᴇᴡs:** {views}\n**📢 ᴄʜᴀɴɴᴇʟ:** {channel_name}",
            duration=dur
        )
        await m.delete()

    except Exception as e:
        await m.edit(f"**❌ ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ:** `{str(e)[:100]}`")
        print(f"Error in download_song: {str(e)}")
    
    finally:
        # Clean up files
        try:
            os.remove(audio_file)
            os.remove(thumb_name)
        except Exception as e:
            print(f"Error cleaning up files: {str(e)}")

def get_text(message: Message) -> [None, str]:
    """Extract command text from message"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    return None

@app.on_message(filters.command(["yt", "video"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    if not urlissed:
        await message.reply("**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠɪᴅᴇᴏ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ**")
        return

    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, f"**🔄 sᴇᴀʀᴄʜɪɴɢ...**")
    
    try:
        search = SearchVideos(urlissed, offset=1, mode="dict", max_results=1)
        mi = search.result()
        mio = mi["search_result"]
        mo = mio[0]["link"]
        thum = mio[0]["title"]
        fridayz = mio[0]["id"]
        thums = mio[0]["channel"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        
        await asyncio.sleep(0.6)
        url = mo
        sedlyf = wget.download(kekme)
        
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
            "outtmpl": os.path.join(TEMP_DIR, "%(id)s.%(ext)s"),
            "logtostderr": False,
            "quiet": True,
        }

        await pablo.edit("**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
        
        with YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            if infoo.get('filesize') and infoo['filesize'] > MAX_FILESIZE:
                await pablo.edit("**⚠️ ғɪʟᴇ sɪᴢᴇ ᴛᴏᴏ ʟᴀʀɢᴇ (>50MB)**")
                return

            duration = round(infoo["duration"] / 60)
            ytdl_data = ytdl.extract_info(url, download=True)

        c_time = time.time()
        file_stark = os.path.join(TEMP_DIR, f"{ytdl_data['id']}.mp4")
        capy = f"**🎥 ᴛɪᴛʟᴇ:** [{thum}]({mo})\n**📢 ᴄʜᴀɴɴᴇʟ:** {thums}\n**🔍 sᴇᴀʀᴄʜᴇᴅ:** {urlissed}\n**👤 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {chutiya}"
        
        await client.send_video(
            message.chat.id,
            video=open(file_stark, "rb"),
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            caption=capy,
            supports_streaming=True,
            progress_args=(
                pablo,
                c_time,
                f"**📤 ᴜᴘʟᴏᴀᴅɪɴɢ** `{urlissed}`",
                file_stark,
            ),
        )
        await pablo.delete()

    except Exception as e:
        await pablo.edit(f"**❌ ᴅᴏᴡɴʟᴏᴀᴅ ғᴀɪʟᴇᴅ:** `{str(e)[:100]}`")
        print(f"Error in ytmusic: {str(e)}")
        
    finally:
        # Clean up files
        for file in (sedlyf, file_stark):
            try:
                if file and os.path.exists(file):
                    os.remove(file)
            except Exception as e:
                print(f"Error cleaning up file {file}: {str(e)}")
