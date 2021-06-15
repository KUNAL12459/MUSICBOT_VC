from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, 𝗜'𝗺 ⚡𝗗3 𝗢𝗣 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧🤟™ ⚡

I can play music in your group's voice call. Developed by [⚡ ❌🔥𝘿3𝙑𝙄𝙇 ✘ 𝗦𝗔𝗜𝗙🔥❌ ⚡](https://t.me/saifalisew1508).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻ 𝗗3 𝗢𝗪𝗡𝗘𝗥 ♻", url="https://t.me/WINZOGOLD_DISCUSS")
                  ],[
                    InlineKeyboardButton(
                        "👤 𝗚𝗥𝗢𝗨𝗣 👤", url="https://t.me/SHIVAM9412")
                    ],[
                    InlineKeyboardButton(
                        "🎛️ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🎛️", url="https://telegra.ph/𝗗3-𝗠𝗨𝗦𝗜𝗖-06-15"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝗔𝗗𝗗 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 ➕", url="https://t.me/D3_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ 𝗗3 𝗢𝗣 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧🤟™ ⚡ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ 𝗠𝗘𝗘𝗧 𝗠𝗬 𝗠𝗔𝗞𝗘𝗥 ❤️", url="https://t.me/saifalisew1508")
                ]
            ]
        )
   )


