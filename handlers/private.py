from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, 𝗜'𝗺 ⚡ 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧🤟™ ⚡

I can play music in your group's voice call. Developed by [⚡𓆩भारतीय𓆪 [• 🇮🇳 •] 𝐒𝐀𝐈𝐅╚»𖣘︎≛━━◤✘#𝐒𝐈𝐌𝐏𝐋𝐄_𝐁𝐎𝐘⚡](https://t.me/saifalisew1508).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 🔥", url="https://t.me/TNR_ON_TOP")
                  ],[
                    InlineKeyboardButton(
                        "🔥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🔥", url="https://t.me/TNRBOLTE")
                    ],[
                    InlineKeyboardButton(
                        "🔰 𝗢𝗪𝗡𝗘𝗥 🔰", url="https://t.me/D3VIL_OP_BOLTE")
                    ],[
                    InlineKeyboardButton(
                        "🎛️ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🎛️", url="https://telegra.ph/𝗗3-𝗠𝗨𝗦𝗜𝗖-06-15"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝗔𝗗𝗗 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 ➕", url="https://t.me/TNR_MUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ 𝗧𝗡𝗥 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 ⚡ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❤️ 𝗠𝗘𝗘𝗧 𝗠𝗬 𝗠𝗔𝗞𝗘𝗥 ❤️", url="https://t.me/saifalisew1508")
                ]
            ]
        )
   )


