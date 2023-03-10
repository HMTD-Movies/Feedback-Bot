# Copyright ÂŠī¸ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!

from pyrogram.types import *

CAPTCHA_BUTT_ONS = [
    [
        InlineKeyboardButton("đĨ",callback_data="đĨ"),
        InlineKeyboardButton("đŠ",callback_data="đŠ"),
        InlineKeyboardButton("đ­",callback_data="đ­"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đĄ", callback_data="đĄ")

    ],
    [

        InlineKeyboardButton("đĄ", callback_data="đĄ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ")
    ],
    [

        InlineKeyboardButton("đ§", callback_data="đ§"),
        InlineKeyboardButton("đ§",callback_data="đ§"),
        InlineKeyboardButton("â",callback_data="â"),
        InlineKeyboardButton("đĒ",callback_data="đĒ"),
        InlineKeyboardButton("đ§¸",callback_data="đ§¸")
    ]
]

CAP1 = [
    [
        InlineKeyboardButton("đĨ",callback_data="đĨ"),
        InlineKeyboardButton("đŠ",callback_data="đŠ"),
        InlineKeyboardButton("đ­",callback_data="đ­"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đĄ", callback_data="đĄ")

    ],
    [

        InlineKeyboardButton("đĄ", callback_data="đĄ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ"),
        InlineKeyboardButton("đ", callback_data="đ")
    ],
    [

        InlineKeyboardButton("â", callback_data="â"),
        InlineKeyboardButton("đ§",callback_data="đ§"),
        InlineKeyboardButton("â",callback_data="â"),
        InlineKeyboardButton("đĒ",callback_data="đĒ"),
        InlineKeyboardButton("đ§¸",callback_data="đ§¸")
    ]
]

WRONG_CAPTCHA  = [
    [
        InlineKeyboardButton("â", callback_data="â")
    ]
]

RELOAD_CAPTCHA = [
    [
        InlineKeyboardButton("Reload CAPTCHA", callback_data="Reload CAPTCHA", url="https://t.me/sanilaassistant_bot?start=start")
    ]
]

PASS_BUTTON = [
    [
        InlineKeyboardButton("â", callback_data="â")
    ]
]
