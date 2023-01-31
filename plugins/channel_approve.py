"""
 This plugin is the part of https://github.com/CyberTG/Queen-autofilter
 License owned by t.me/AFxSU
 All credits belongs tohttps://github.com/CyberTG
 Modification are welcome (under license)
 Code crated by @AFxSU
"""
# header file
import time
import asyncio
from os import environ as evn
from pyrogram import Client as bin, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

#function

@bin.on_chat_join_request(filters.group | filters.channel)
async def autoapprove(c, m):
    await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    button = [[
        InlineKeyboardButton('🎬JOIN MOVIE CHANNEL🎬', url='https://t.me/at3moviesofficalbot')
        ],[
        InlineKeyboardButton('📽️JOIN MOVIE GROUP📽️', url='https://t.me/MovieGroup_TM')
        ]]
    markup = InlineKeyboardMarkup(button)
    caption = f'Hello {m.from_user.mention()}\nYou Request To Join {m.chat.title} Was Approved.'
    await c.send_photo(
        m.from_user.id, 
        photo='https://telegra.ph/file/f7738f04ea74e16c9db02.jpg', 
        caption=caption, 
        reply_markup=markup
    )
