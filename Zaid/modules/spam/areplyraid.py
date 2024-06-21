import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from Zaid.database.rraid import *
from Zaid import SUDO_USER
from pyrogram import errors
from pyrogram.types import ChatPermissions, Message
DEVS = int(7374966263)
from Zaid.helper.PyroHelpers import get_ub_chats
from Zaid.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS

@Client.on_message(
    filters.command(["rraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    
    ex = await message.reply_text("`Processing...`")  # Changed to reply_text to create a new message
    
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit_text(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit_text(f"`Please specify a valid user!`")
        return

    if user.id == client.me.id:
        return await ex.edit_text("**Okay Sure.. 🐽**")
    elif user.id == SUDO_USERS:
        return await ex.edit_text("**Okay But Failed Because this user in sudos.. 🐽**")
    elif user.id == VERIFIED_USERS:
        return await ex.edit_text("**Chal Chal Baap ko Mat sikha.. 🐽**")
    
    try:
        if user.id in (await get_rraid_users()):
            await ex.edit_text("Replyraid is activated on this user")
            return
        await rraid_user(user.id)
        RAIDS.append(user.id)
        await ex.edit_text(f"[{user.first_name}](tg://user?id={user.id}) Activated ReplyRaid!")
    except Exception as e:
        await ex.edit_text(f"**ERROR:** `{e}`")
        return
