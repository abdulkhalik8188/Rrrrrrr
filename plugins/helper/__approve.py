import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid


##@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
@Client.on_chat_join_request(filters.group | filters.channel)
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[
            InlineKeyboardButton('albin', url=f'https://t.me/albin')
            
        ]]
        markup = InlineKeyboardMarkup(button)
        caption = f'Hello {m.from_user.mention()}\nYou Request To Join {m.chat.title} Was Approved.'
        await client.send_photo(
            m.from_user.id, 
            photo='https://te.legra.ph/file/94d8bfbda46bcf2415346.jpg', 
            caption=caption, 
            reply_markup=markup
        )
        except UserIsBlocked:
        print(f"{m.from_user.first_name} blocked the bot")
    except PeerIdInvalid:
        print(f"User {m.from_user.first_name} haven't started the bot yet")
    except Exception as e:
        print('Error:', e)

    
