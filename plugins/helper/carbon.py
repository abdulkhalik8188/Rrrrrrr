from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import gather
from datetime import datetime, timedelta
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from os import execvp
from random import randint
from re import findall
from re import sub as re_sub
from sys import executable
import aiofiles
import speedtest
from PIL import Image
from pyrogram.types import Message
from info import S_GROUP

aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption="**ᴛʜɪs ᴘɪᴄ ɪs ɴɪᴄᴇ ᴏɴᴇ\nᴍᴀᴅᴇ ʙʏ 𝙼𝙾𝚅𝙸𝙴𝚂 𝙵𝙻𝙸𝚇**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=S_GROUP)]]),                   
    )
    await m.delete()
    carbon.close()
