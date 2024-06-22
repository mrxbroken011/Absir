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
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(7374966263)
from Zaid.helper.PyroHelpers import get_ub_chats
from Zaid.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS

@Client.on_message(
    filters.command(["reraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    sent_message = await message.reply("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await sent_message.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await sent_message.edit(f"`Please specify a valid user!`")
        return

    if user.id == client.me.id:
        return await sent_message.edit("**Okay Sure.. 🐽**")
    elif user.id in SUDO_USERS:
        return await sent_message.edit("**Okay But Failed Because this user is in sudos.. 🐽**")
    elif user.id in VERIFIED_USERS:
        return await sent_message.edit("**Chal Chal Baap ko Mat sikha.. 🐽**")

    try:
        if user.id in (await get_rraid_users()):
            await sent_message.edit("Replyraid is already activated on this user")
            return
        await rraid_user(user.id)
        RAIDS.append(user.id)
        await sent_message.edit(f"[{user.first_name}](tg://user?id={user.id}) Activated ReplyRaid!")
    except Exception as e:
        await sent_message.edit(f"**ERROR:** `{e}`")
        return
