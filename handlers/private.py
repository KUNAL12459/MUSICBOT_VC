from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, ๐'๐บ โก ๐ ๐จ๐ฆ๐๐ ๐๐ข๐ง๐คโข โก

I can play music in your group's voice call. Developed by [โก๐ฉเคญเคพเคฐเคคเฅเคฏ๐ช [โข ๐ฎ๐ณ โข] ๐๐๐๐โยป๐ฃ๏ธโโโโคโ#๐๐๐๐๐๐_๐๐๐โก](https://t.me/saifalisew1508).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ ๐ฆ๐จ๐ฃ๐ฃ๐ข๐ฅ๐ง ๐๐ฅ๐ข๐จ๐ฃ ๐ฅ", url="https://t.me/TNR_ON_TOP")
                  ],[
                    InlineKeyboardButton(
                        "๐ฅ ๐ฆ๐จ๐ฃ๐ฃ๐ข๐ฅ๐ง ๐๐๐๐ก๐ก๐๐ ๐ฅ", url="https://t.me/TNRBOLTE")
                    ],[
                    InlineKeyboardButton(
                        "๐ฐ ๐ข๐ช๐ก๐๐ฅ ๐ฐ", url="https://t.me/D3VIL_OP_BOLTE")
                    ],[
                    InlineKeyboardButton(
                        "๐๏ธ ๐๐ข๐ ๐ ๐๐ก๐๐ฆ ๐๏ธ", url="https://telegra.ph/๐3-๐ ๐จ๐ฆ๐๐-06-15"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐ง๐ข ๐ฌ๐ข๐จ๐ฅ ๐๐ฅ๐ข๐จ๐ฃ โ", url="https://t.me/TNR_MUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**โก ๐ง๐ก๐ฅ ๐ ๐จ๐ฆ๐๐ ๐๐ข๐ง โก is on fire ๐ฅ โ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โค๏ธ ๐ ๐๐๐ง ๐ ๐ฌ ๐ ๐๐๐๐ฅ โค๏ธ", url="https://t.me/saifalisew1508")
                ]
            ]
        )
   )


