from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, 𝗜'𝗺 ⚡𝚆𝙸𝙽𝚉𝙾 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃™ ⚡

I can play music in your group's voice call. Developed by [⚡ 𝚅𝙴𝙽𝙾𝙼 𝚂𝙷𝙸𝚅𝙰𝙼 ⚡](https://t.me/SHIVAM9412).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃♻", url="https://t.me/WINZOGOLD_DISCUSS")
                  ],[
                    InlineKeyboardButton(
                        "👤 𝙾𝚆𝙽𝙴𝚁 👤", url="https://t.me/SHIVAM9412")
                    ],[
                    InlineKeyboardButton(
                        "🎛️ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 🎛️", url="https://telegra.ph/ANSHIKA-MUSIC-05-24-2"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕", url="https://t.me/winzo_musicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ 𝚆𝙸𝙽𝚉𝙾 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 ™ ⚡ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ 𝙼𝙾𝙸 𝙾𝙿 𝙼𝙰𝚂𝚃𝙴𝚁 ❤️", url="https://t.me/SHIVAM9412")
                ]
            ]
        )
   )


