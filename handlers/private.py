from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, 𝗜'𝗺 ⚡ ANSHIKA MUSIC BOT ™ ⚡

I can play music in your group's voice call. Developed by [⚡ ANSHIKA SINGH ⚡](https://t.me/@nshikasingh_4).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻ SUPPORT GROUP ♻", url="https://t.me/schoolmastii")
                  ],[
                    InlineKeyboardButton(
                        "👤 CONTACT OWNER 👤", url="https://t.me/Anshikasingh_4")
                    ],[
                    InlineKeyboardButton(
                        "🎛️ COMMANDS 🎛️", url="https://telegra.ph/ANSHIKA-MUSIC-05-24-2"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ADD TO YOUR GROUP ➕", url="https://t.me/ANSHIKAMUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ ANSHIKA MUSIC BOT ™ ⚡ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ MY CREATOR ❤️", url="https://t.me/Anshikasingh_4")
                ]
            ]
        )
   )


