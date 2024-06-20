from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC

PHONE_NUMBER_TEXT = (
    "✘ Heya My Master👋!\n\n"
    "✘ I'm Your Assistant?\n\n"
    "‣ I can help you to host Your Left Clients.\n\n"
    "‣ Repo: github.com/Itz-Zaid/Zaid-Userbot \n\n"
    "‣ This specially for Buzzy People's(lazy)\n\n"
    "‣ Now /clone {send your PyroGram String Session}"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheUpdatesChannel")],
        [InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/TheSupportChat")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: Client, msg: Message):
    if len(msg.command) < 2:
        await msg.reply("Usage:\n\n /clone session")
        return
    
    phone = msg.command[1]
    text = await msg.reply("Booting Your Client")

    try:
        # Initialize and start the new client
        new_client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=phone,
            plugins=dict(root="Zaid/modules")
        )
        await new_client.start()
        
        # Retrieve and send the user information
        user = await new_client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started as {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
