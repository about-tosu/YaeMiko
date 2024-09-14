# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/df910c1a7c251c298f4b5.jpg",
    "https://graph.org/file/df910c1a7c251c298f4b5.jpg",
    "https://telegra.ph/file/50da5116b6d31ae9ca840.jpg",
    "https://telegra.ph/file/50da5116b6d31ae9ca840.jpg",
    "https://graph.org/file/df910c1a7c251c298f4b5.jpg",
    "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg",
    "https://graph.org/file/df910c1a7c251c298f4b5.jpg",
]

HEY_IMG = "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg"

ALIVE_ANIMATION = [
    "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg",
    "https://graph.org/file/df910c1a7c251c298f4b5.jpg",
    "https://telegra.ph/file/50da5116b6d31ae9ca840.jpg",
    "https://telegra.ph/file/50da5116b6d31ae9ca840.jpg",
    "https://graph.org/file/a89a03efc7f4bf077a4a6.jpg",
    "https://telegra.ph/file/265a628a568d7a902057a.jpg",
    "https://telegra.ph/file/2829138cd6da27fcae483.jpg",
    "https://telegra.ph/file/265a628a568d7a902057a.jpg",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ᴍɪᴋᴏ, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/about_tosuu"),
        ib(text="SUPPORT", url="https://t.me/nothing_bots_support"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
