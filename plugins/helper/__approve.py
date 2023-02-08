import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[
            InlineKeyboardButton('albin', url=f'https://t.me/albin')
            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
