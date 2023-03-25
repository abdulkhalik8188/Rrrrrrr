import wikipedia
from pyrogram import Client, filters

@Client.on_message(filters.command('wikipedia'))
async def wiki(Client, message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    if user_request == "":
        wikipedia.set_lang("en")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "ml":
            wikipedia.set_lang("ml")

        result = wikipedia.summary(user_request)
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{result}</code>"""
        )

    except Exception as exc:
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>"""
        )
