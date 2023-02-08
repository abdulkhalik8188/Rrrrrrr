import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from info import CHAT_ID, TEXT, APPROVED 


            
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('pling', url='https://wikipedia.org),
            InlineKeyboardButton('plong', url='https://wa.me+9196542 97000')
        ]
    ]
)

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
    await client.send_message(
        text=TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=False,
        reply_markup=BUTTONS
    ) 

    
