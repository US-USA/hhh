from pyrogram import filters
from pyrogram import Client as BOTidSBot
from BOTidSBot.Translation import Translation
from BOTidSBot.echobot import echobot

BOT_USERNAME=Config.BOT_USERNAME

@BOTidSBot.on_callback_query()
async def cb_handler(client, query):

    if query.data == "id":
        await query.answer()
        await query.message.edit_text(
            Translation.ID_TEXT.format(query.from_user.id)
            disable_web_page_preview=True
        )
        return

    elif query.data == "close":
        await query.message.delete()
