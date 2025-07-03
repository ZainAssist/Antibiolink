"""
Author: Zainu
User: https://t.me/Uff_Zainu
Channel: https://t.me/About_Zain
"""

from pyrogram import Client, filters, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions

from helper.utils import (
    is_admin,
    get_config, update_config,
    increment_warning, reset_warnings,
    is_whitelisted, add_whitelist, remove_whitelist, get_whitelist
)

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    URL_PATTERN,
    START_IMG_URL,
    HELP_IMG_URL,
    CONFIG_IMG_URL,
    BOT_OWNER,
    BOT_OWNER_USERNAME
)

from broadcast import register_broadcast_handlers  # Add this import

app = Client(
    "Antibiolink",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

register_broadcast_handlers(app)  # Register broadcast handlers

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message):
    chat_id = message.chat.id
    bot = await client.get_me()
    add_url = f"https://t.me/{bot.username}?startgroup=true"
    
    # Send start image
    try:
        await client.send_photo(
            chat_id=chat_id,
            photo=START_IMG_URL,  # Use the configured URL instead of hardcoded one
            caption=(
                "**✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀɴᴛɪʙɪᴏʟɪɴᴋ ʙᴏᴛ! ✨**\n\n"
                "🛡️ ɪ ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғʀᴏᴍ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ᴛʜᴇɪʀ ʙɪᴏ.\n\n"
                "**🔹 ᴋᴇʏ ғᴇᴀᴛᴜʀᴇs:**\n"
                "   • ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴜʀʟ ᴅᴇᴛᴇᴄᴛɪᴏɴ ɪɴ ᴜsᴇʀ ʙɪᴏs\n"
                "   • ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴀʀɴɪɴɡ ʟɪᴍɪᴛ\n"
                "   • ᴀᴜᴛᴏ-ᴍᴜᴛᴇ ᴏʀ ʙᴀɴ ᴡʜᴇɴ ʟɪᴍɪᴛ ɪs ʀᴇᴀᴄʜᴇᴅ\n"
                "   • ᴡʜɪᴛᴇʟɪsᴛ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ғᴏʀ ᴛʀᴜsᴛᴇᴅ ᴜsᴇʀs\n\n"
                "**ᴜsᴇ /help ᴛᴏ sᴇᴇ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.**"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=add_url)],
                [
                    InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/About_Zain"),
                    InlineKeyboardButton("🧑‍💻 ᴏᴡɴᴇʀ", url=f"https://t.me/{BOT_OWNER_USERNAME}" if BOT_OWNER_USERNAME else f"tg://user?id={BOT_OWNER}")
                ],
                [InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
            ])
        )
    except Exception as e:
        print(f"Error sending image: {e}")  # Added logging for debugging
        # Fallback to text message if image sending fails
        text = (
            "**✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀɴᴛɪʙɪᴏʟɪɴᴋ ʙᴏᴛ! ✨**\n\n"
            "🛡️ ɪ ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғʀᴏᴍ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ᴛʜᴇɪʀ ʙɪᴏ.\n\n"
            "**🔹 ᴋᴇʏ ғᴇᴀᴛᴜʀᴇs:**\n"
            "   • ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴜʀʟ ᴅᴇᴛᴇᴄᴛɪᴏɴ ɪɴ ᴜsᴇʀ ʙɪᴏs\n"
            "   • ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴀʀɴɪɴɡ ʟɪᴍɪᴛ\n"
            "   • ᴀᴜᴛᴏ-ᴍᴜᴛᴇ ᴏʀ ʙᴀɴ ᴡʜᴇɴ ʟɪᴍɪᴛ ɪs ʀᴇᴀᴄʜᴇᴅ\n"
            "   • ᴡʜɪᴛᴇʟɪsᴛ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ғᴏʀ ᴛʀᴜsᴛᴇᴅ ᴜsᴇʀs\n\n"
            "**ᴜsᴇ /help ᴛᴏ sᴇᴇ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.**"
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=add_url)],
            [
                InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ", url="https://t.me/About_Zain"),
                InlineKeyboardButton("🧑‍💻 ᴏᴡɴᴇʀ", url=f"https://t.me/{BOT_OWNER_USERNAME}" if BOT_OWNER_USERNAME else f"tg://user?id={BOT_OWNER}")
            ],
            [InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
        ])
        await client.send_message(chat_id, text, reply_markup=kb)
    
@app.on_message(filters.command("help"))
async def help_handler(client: Client, message):
    chat_id = message.chat.id
    help_text = (
        "**🛠️ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs & ᴜsᴀɢᴇ**\n\n"
        "`/config` – sᴇᴛ ᴡᴀʀɴ-ʟɪᴍɪᴛ & ᴘᴜɴɪsʜᴍᴇɴᴛ ᴍᴏᴅᴇ\n"
        "`/free` – ᴡʜɪᴛᴇʟɪsᴛ ᴀ ᴜsᴇʀ (ʀᴇᴘʟʏ ᴏʀ ᴜsᴇʀ/ɪᴅ)\n"
        "`/unfree` – ʀᴇᴍᴏᴠᴇ ғʀᴏᴍ ᴡʜɪᴛᴇʟɪsᴛ\n"
        "`/freelist` – ʟɪsᴛ ᴀʟʟ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ ᴜsᴇʀs\n\n"
        "**ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴡɪᴛʜ ᴀ ᴜʀʟ ɪɴ ᴛʜᴇɪʀ ʙɪᴏ ᴘᴏsᴛs, ɪ'ʟʟ:**\n"
        " 1. ⚠️ ᴡᴀʀɴ ᴛʜᴇᴍ\n"
        " 2. 🔇 ᴍᴜᴛᴇ ɪғ ᴛʜᴇʏ ᴇxᴄᴇᴇᴅ ʟɪɱɪᴛ\n"
        " 3. 🔨 ʙᴀɴ ɪғ sᴇᴛ ᴛᴏ ʙᴀɴ\n\n"
        "**ᴜsᴇ ᴛʜᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs ᴏɴ ᴡᴀʀɴɪɴɡs ᴛᴏ ᴄᴀɴᴄᴇʟ ᴏʀ ᴡʜɪᴛᴇʟɪsᴛ**"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
    ])
    
    # Import HELP_IMG_URL from config.py
    from config import HELP_IMG_URL
    
    # Send help image
    try:
        await client.send_photo(
            chat_id=chat_id,
            photo=HELP_IMG_URL,  # Use the configured URL instead of hardcoded one
            caption=help_text,
            reply_markup=kb
        )
    except Exception as e:
        print(f"Error sending help image: {e}")  # Added logging for debugging
        # Fallback to text message if image sending fails
        await client.send_message(chat_id, help_text, reply_markup=kb)

@app.on_message(filters.group & filters.command("config"))
async def configure(client: Client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not await is_admin(client, chat_id, user_id):
        return

    mode, limit, penalty = await get_config(chat_id)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴡᴀʀɴ", callback_data="warn")],
        [
            InlineKeyboardButton("ᴍᴜᴛᴇ ✅" if penalty == "mute" else "ᴍᴜᴛᴇ", callback_data="mute"),
            InlineKeyboardButton("ʙᴀɴ ✅" if penalty == "ban" else "ʙᴀɴ", callback_data="ban")
        ],
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
    ])
    
    # Import CONFIG_IMG_URL from config.py
    from config import CONFIG_IMG_URL
    
    # Send config with image
    try:
        await client.send_photo(
            chat_id=chat_id,
            photo=CONFIG_IMG_URL,  # Use the configured URL instead of hardcoded one
            caption="**ᴄʜᴏᴏsᴇ ᴘᴇɴᴀʟᴛʏ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ʙɪᴏ:**",
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Error sending config image: {e}")  # Added logging for debugging
        # Fallback to text message if image sending fails
        await client.send_message(
            chat_id,
            "**ᴄʜᴏᴏsᴇ ᴘᴇɴᴀʟᴛʏ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ʙɪᴏ:**",
            reply_markup=keyboard
        )
    
    await message.delete()

@app.on_message(filters.group & filters.command("free"))
async def command_free(client: Client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not await is_admin(client, chat_id, user_id):
        return

    if message.reply_to_message:
        target = message.reply_to_message.from_user
    elif len(message.command) > 1:
        arg = message.command[1]
        target = await client.get_users(int(arg) if arg.isdigit() else arg)
    else:
        return await client.send_message(chat_id, "**ʀᴇᴘʟʏ ᴏʀ ᴜsᴇ /free ᴜsᴇʀ ᴏʀ ɪᴅ ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ sᴏᴍᴇᴏɴᴇ.**")

    await add_whitelist(chat_id, target.id)
    await reset_warnings(chat_id, target.id)

    text = f"**✅ {target.mention} ʜᴀs ʙᴇᴇɪɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴡʜɪᴛᴇʟɪsᴛ**"
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🚫 ᴜɴᴡʜɪᴛᴇʟɪsᴛ", callback_data=f"unwhitelist_{target.id}"),
            InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")
        ]
    ])
    await client.send_message(chat_id, text, reply_markup=keyboard)

@app.on_message(filters.group & filters.command("unfree"))
async def command_unfree(client: Client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not await is_admin(client, chat_id, user_id):
        return

    if message.reply_to_message:
        target = message.reply_to_message.from_user
    elif len(message.command) > 1:
        arg = message.command[1]
        target = await client.get_users(int(arg) if arg.isdigit() else arg)
    else:
        return await client.send_message(chat_id, "**ʀᴇᴘʟʏ ᴏʀ ᴜsᴇ /unfree ᴜsᴇʀ ᴏʀ ɪᴅ ᴛᴏ ᴜɴᴡʜɪᴛᴇʟɪsᴛ sᴏᴍᴇᴏɴᴇ.**")

    if await is_whitelisted(chat_id, target.id):
        await remove_whitelist(chat_id, target.id)
        text = f"**🚫 {target.mention} ʜᴀs ʙᴇᴇɪɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴡʜɪᴛᴇʟɪsᴛ**"
    else:
        text = f"**ℹ️ {target.mention} ɪs ɴᴏᴛ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ.**"

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ ᴡʜɪᴛᴇʟɪsᴛ", callback_data=f"whitelist_{target.id}"),
            InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")
        ]
    ])
    await client.send_message(chat_id, text, reply_markup=keyboard)

@app.on_message(filters.group & filters.command("freelist"))
async def command_freelist(client: Client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if not await is_admin(client, chat_id, user_id):
        return

    ids = await get_whitelist(chat_id)
    if not ids:
        await client.send_message(chat_id, "**⚠️ ɴᴏ ᴜsᴇʀs ᴀʀᴇ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")
        return

    text = "**📋 ᴡʜɪᴛᴇʟɪsᴛᴇᴅ ᴜsᴇʀs:**\n\n"
    for i, uid in enumerate(ids, start=1):
        try:
            user = await client.get_users(uid)
            name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
            text += f"{i}: {name} [`{uid}`]\n"
        except:
            text += f"{i}: [ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ] [`{uid}`]\n"

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]])
    await client.send_message(chat_id, text, reply_markup=keyboard)

@app.on_callback_query()
async def callback_handler(client: Client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    if not await is_admin(client, chat_id, user_id):
        return await callback_query.answer("❌ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ", show_alert=True)

    if data == "close":
        return await callback_query.message.delete()

    if data == "back":
        mode, limit, penalty = await get_config(chat_id)
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴡᴀʀɴ", callback_data="warn")],
            [
                InlineKeyboardButton("ᴍᴜᴛᴇ ✅" if penalty=="mute" else "ᴍᴜᴛᴇ", callback_data="mute"),
                InlineKeyboardButton("ʙᴀɴ ✅" if penalty=="ban" else "ʙᴀɴ", callback_data="ban")
            ],
            [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        ])
        try:
            # Try to send/edit with image
            if callback_query.message.photo:
                await callback_query.message.edit_caption(
                    caption="**ᴄʜᴏᴏsᴇ ᴘᴇɴᴀʟᴛʏ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ʙɪᴏ:**",
                    reply_markup=kb
                )
            else:
                # If original message doesn't have photo, edit text only
                await callback_query.message.edit_text("**ᴄʜᴏᴏsᴇ ᴘᴇɴᴀʟᴛʏ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ʙɪᴏ:**", reply_markup=kb)
        except Exception as e:
            print(f"Error updating callback message: {e}")  # Added logging for debugging
            # Fallback if edit fails
            await callback_query.message.edit_text("**ᴄʜᴏᴏsᴇ ᴘᴇɴᴀʟᴛʏ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ ʟɪɴᴋs ɪɴ ʙɪᴏ:**", reply_markup=kb)
        return await callback_query.answer()

    if data == "warn":
        _, selected_limit, _ = await get_config(chat_id)
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"3 ✅" if selected_limit==3 else "3", callback_data="warn_3"),
             InlineKeyboardButton(f"4 ✅" if selected_limit==4 else "4", callback_data="warn_4"),
             InlineKeyboardButton(f"5 ✅" if selected_limit==5 else "5", callback_data="warn_5")],
            [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back"), InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        ])
        try:
            # Try to edit with image if present
            if callback_query.message.photo:
                return await callback_query.message.edit_caption(
                    caption="**sᴇʟᴇᴄᴛ ɴᴜᴍʙᴇʀ ᴏғ ᴡᴀʀɴs ʙᴇғᴏʀᴇ ᴘᴇɴᴀʟᴛʏ:**", 
                    reply_markup=kb
                )
            else:
                return await callback_query.message.edit_text("**sᴇʟᴇᴄᴛ ɴᴜᴍʙᴇʀ ᴏғ ᴡᴀʀɴs ʙᴇғᴏʀᴇ ᴘᴇɴᴀʟᴛʏ:**", reply_markup=kb)
        except Exception as e:
            return await callback_query.message.edit_text("**sᴇʟᴇᴄᴛ ɴᴜᴍʙᴇʀ ᴏғ ᴡᴀʀɴs ʙᴇғᴏʀᴇ ᴘᴇɴᴀʟᴛʏ:**", reply_markup=kb)

    if data in ["mute", "ban"]:
        await update_config(chat_id, penalty=data)
        mode, limit, penalty = await get_config(chat_id)
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴡᴀʀɴ", callback_data="warn")],
            [
                InlineKeyboardButton("ᴍᴜᴛᴇ ✅" if penalty=="mute" else "ᴍᴜᴛᴇ", callback_data="mute"),
                InlineKeyboardButton("ʙᴀɴ ✅" if penalty=="ban" else "ʙᴀɴ", callback_data="ban")
            ],
            [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        ])
        try:
            # Try to edit with image if present
            if callback_query.message.photo:
                await callback_query.message.edit_caption(caption="**ᴘᴜɴɪsʜᴍᴇɴᴛ sᴇʟᴇᴄᴛᴇᴅ:**", reply_markup=kb)
            else:
                await callback_query.message.edit_text("**ᴘᴜɴɪsʜᴍᴇɴᴛ sᴇʟᴇᴄᴛᴇᴅ:**", reply_markup=kb)
        except Exception as e:
            await callback_query.message.edit_text("**ᴘᴜɴɪsʜᴍᴇɴᴛ sᴇʟᴇᴄᴛᴇᴅ:**", reply_markup=kb)
        return await callback_query.answer()

    if data.startswith("warn_"):
        count = int(data.split("_")[1])
        await update_config(chat_id, limit=count)
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"3 ✅" if count==3 else "3", callback_data="warn_3"),
             InlineKeyboardButton(f"4 ✅" if count==4 else "4", callback_data="warn_4"),
             InlineKeyboardButton(f"5 ✅" if count==5 else "5", callback_data="warn_5")],
            [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back"), InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        ])
        try:
            # Try to edit with image if present
            if callback_query.message.photo:
                await callback_query.message.edit_caption(
                    caption=f"**ᴡᴀʀɴɪɴɡ ʟɪᴍɪᴛ sᴇᴛ ᴛᴏ {count}**", 
                    reply_markup=kb
                )
            else:
                await callback_query.message.edit_text(f"**ᴡᴀʀɴɪɴɡ ʟɪᴍɪᴛ sᴇᴛ ᴛᴏ {count}**", reply_markup=kb)
        except Exception as e:
            await callback_query.message.edit_text(f"**ᴡᴀʀɴɪɴɡ ʟɪᴍɪᴛ sᴇᴛ ᴛᴏ {count}**", reply_markup=kb)
        return await callback_query.answer()

    if data.startswith(("unmute_", "unban_")):
        action, uid = data.split("_")
        target_id = int(uid)
        user = await client.get_chat(target_id)
        name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
        try:
            if action == "unmute":
                await client.restrict_chat_member(chat_id, target_id, ChatPermissions(can_send_messages=True))
            else:
                await client.unban_chat_member(chat_id, target_id)
            await reset_warnings(chat_id, target_id)
            msg = f"**{name} (`{target_id}`) ʜᴀs ʙᴇᴇɪɴ {'ᴜɴᴍᴜᴛᴇᴅ' if action=='unmute' else 'ᴜɴʙᴀɴɴᴇᴅ'}**."

            kb = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("ᴡʜɪᴛᴇʟɪsᴛ ✅", callback_data=f"whitelist_{target_id}"),
                    InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")
                ]
            ])
            await callback_query.message.edit_text(msg, reply_markup=kb)
        
        except errors.ChatAdminRequired:
            await callback_query.message.edit_text(f"ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ {action} ᴜsᴇʀs.")
        return await callback_query.answer()

    if data.startswith("cancel_warn_"):
        target_id = int(data.split("_")[-1])
        await reset_warnings(chat_id, target_id)
        user = await client.get_chat(target_id)
        full_name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
        mention = f"[{full_name}](tg://user?id={target_id})"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴡʜɪᴛᴇʟɪsᴛ✅", callback_data=f"whitelist_{target_id}"),
             InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
        ])
        await callback_query.message.edit_text(f"**✅ {mention} [`{target_id}`] ʜᴀs ɴᴏ ᴍᴏʀᴇ ᴡᴀʀɴɪɴɡs!**", reply_markup=kb)
        return await callback_query.answer()

    if data.startswith("whitelist_"):
        target_id = int(data.split("_")[1])
        await add_whitelist(chat_id, target_id)
        await reset_warnings(chat_id, target_id)
        user = await client.get_chat(target_id)
        full_name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
        mention = f"[{full_name}](tg://user?id={target_id})"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🚫 ᴜɴᴡʜɪᴛᴇʟɪsᴛ", callback_data=f"unwhitelist_{target_id}"),
             InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
        ])
        await callback_query.message.edit_text(f"**✅ {mention} [`{target_id}`] ʜᴀs ʙᴇᴇɪɴ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ!**", reply_markup=kb)
        return await callback_query.answer()

    if data.startswith("unwhitelist_"):
        target_id = int(data.split("_")[1])
        await remove_whitelist(chat_id, target_id)
        user = await client.get_chat(target_id)
        full_name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
        mention = f"[{full_name}](tg://user?id={target_id})"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴡʜɪᴛᴇʟɪsᴛ✅", callback_data=f"whitelist_{target_id}"),
             InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
        ])
        await callback_query.message.edit_text(f"**❌ {mention} [`{target_id}`] ʜᴀs ʙᴇᴇɪɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴡʜɪᴛᴇʟɪsᴛ.**", reply_markup=kb)
        return await callback_query.answer()

@app.on_message(filters.group)
async def check_bio(client: Client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if await is_admin(client, chat_id, user_id) or await is_whitelisted(chat_id, user_id):
        return

    user = await client.get_chat(user_id)
    bio = user.bio or ""
    full_name = f"{user.first_name}{(' ' + user.last_name) if user.last_name else ''}"
    mention = f"[{full_name}](tg://user?id={user_id})"

    if URL_PATTERN.search(bio):
        try:
            await message.delete()
        except errors.MessageDeleteForbidden:
            return await message.reply_text("ᴘʟᴇᴀsᴇ ɢʀᴀɴᴛ ᴍᴇ ᴅᴇʟᴇᴛᴇ ᴘᴇʀᴍɪssɪᴏɴ.")

        mode, limit, penalty = await get_config(chat_id)
        if mode == "warn":
            count = await increment_warning(chat_id, user_id)
            warning_text = (
                "**🚨 ᴡᴀʀɴɪɴɢ ɪssᴜᴇᴅ** 🚨\n\n"
                f"👤 **ᴜsᴇʀ:** {mention} `[{user_id}]`\n"
                "❌ **ʀᴇᴀsᴏɴ:** ᴜʀʟ ғᴏᴜɴᴅ ɪɴ ʙɪᴏ\n"
                f"⚠️ **ᴡᴀʀɴɪɴɡ:** {count}/{limit}\n\n"
                "**ɴᴏᴛɪᴄᴇ: ᴘʟᴇᴀsᴇ ʀᴇᴍᴏᴠᴇ ᴀɴʏ ʟɪɴᴋs ғʀᴏᴍ ʏᴏᴜʀ ʙɪᴏ.**"
            )
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ᴡᴀʀɴɪɴɢ", callback_data=f"cancel_warn_{user_id}"),
                 InlineKeyboardButton("✅ ᴡʜɪᴛᴇʟɪsᴛ", callback_data=f"whitelist_{user_id}")],
                [InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
            ])
            sent = await message.reply_text(warning_text, reply_markup=keyboard)
            if count >= limit:
                try:
                    if penalty == "mute":
                        await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
                        kb = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜɴᴍᴜᴛᴇ ✅", callback_data=f"unmute_{user_id}")]])
                        await sent.edit_text(f"**{mention} ʜᴀs ʙᴇᴇɪɴ 🔇 ᴍᴜᴛᴇᴅ ғᴏʀ [ʟɪɴᴋ ɪɴ ʙɪᴏ].**", reply_markup=kb)
                    else:
                        await client.ban_chat_member(chat_id, user_id)
                        kb = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜɴʙᴀɴ ✅", callback_data=f"unban_{user_id}")]])
                        await sent.edit_text(f"**{mention} ʜᴀs ʙᴇᴇɪɴ 🔨 ʙᴀɴɴᴇᴅ ғᴏʀ [ʟɪɴᴋ ɪɴ ʙɪᴏ].**", reply_markup=kb)
                
                except errors.ChatAdminRequired:
                    await sent.edit_text(f"**ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ {penalty} ᴜsᴇʀs.**")
        else:
            try:
                if mode == "mute":
                    await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
                    kb = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜɴᴍᴜᴛᴇ", callback_data=f"unmute_{user_id}")]])
                    await message.reply_text(f"{mention} ʜᴀs ʙᴇᴇɪɴ 🔇 ᴍᴜᴛᴇᴅ ғᴏʀ [ʟɪɴᴋ ɪɴ ʙɪᴏ].", reply_markup=kb)
                else:
                    await client.ban_chat_member(chat_id, user_id)
                    kb = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜɴʙᴀɴ", callback_data=f"unban_{user_id}")]])
                    await message.reply_text(f"{mention} ʜᴀs ʙᴇᴇɪɴ 🔨 ʙᴀɴɴᴇᴅ ғᴏʀ [ʟɪɴᴋ ɪɴ ʙɪᴏ].", reply_markup=kb)
            except errors.ChatAdminRequired:
                return await message.reply_text(f"ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ {mode} ᴜsᴇʀs.")
    else:
        await reset_warnings(chat_id, user_id)

if __name__ == "__main__":
    app.run()
