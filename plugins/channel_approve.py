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



