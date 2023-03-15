import time
import random
from pyrogram import Client, filters
from Script import script

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 😁")

@Client.on_message(filters.command("extra", CMD))
async def extra(_, message):
    await message.reply_text(script.EXTRA_TXT)


@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    await message.reply_text("😎")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")

