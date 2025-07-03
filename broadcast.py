import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait

# from bio import app  # REMOVE this import to avoid circular import
from helper.utils import get_config, get_whitelist
from helper.utils import db  # Use the db object from utils.py

IS_BROADCASTING = False

async def get_all_chat_ids():
    # Get all unique chat_id from the whitelists collection
    chat_ids = await db['whitelists'].distinct('chat_id')
    return chat_ids

async def get_all_user_ids():
    # Get all unique user_id from the whitelists collection
    user_ids = await db['whitelists'].distinct('user_id')
    return user_ids

def register_broadcast_handlers(app):
    @app.on_message(filters.command("broadcast"))
    async def broadcast_message(client, message):
        global IS_BROADCASTING

        # Only allow the bot owner to broadcast
        from config import BOT_OWNER
        if not message.from_user or message.from_user.id != BOT_OWNER:
            return await message.reply_text("You are not authorized to use this command.")

        if not message.reply_to_message:
            return await message.reply_text("Please reply to a message to broadcast.")

        IS_BROADCASTING = True
        await message.reply_text("Broadcast started...")

        sent_chats = 0
        sent_users = 0

        # Broadcast to all chats
        chat_ids = await get_all_chat_ids()
        if not chat_ids:
            await message.reply_text("No chats found to broadcast.")
        else:
            for chat_id in chat_ids:
                try:
                    await client.copy_message(chat_id, message.chat.id, message.reply_to_message.id)
                    sent_chats += 1
                    await asyncio.sleep(0.2)
                except FloodWait as fw:
                    wait_time = fw.value if isinstance(fw.value, int) else 5
                    await asyncio.sleep(wait_time)
                except Exception as e:
                    print(f"Error sending to chat {chat_id}: {e}")
                    continue

        # Broadcast to all users
        user_ids = await get_all_user_ids()
        if not user_ids:
            await message.reply_text("No users found to broadcast.")
        else:
            for user_id in user_ids:
                try:
                    await client.copy_message(user_id, message.chat.id, message.reply_to_message.id)
                    sent_users += 1
                    await asyncio.sleep(0.2)
                except FloodWait as fw:
                    wait_time = fw.value if isinstance(fw.value, int) else 5
                    await asyncio.sleep(wait_time)
                except Exception as e:
                    print(f"Error sending to user {user_id}: {e}")
                    continue

        try:
            await message.reply_text(f"Broadcast completed! Sent to {sent_chats} chats and {sent_users} users.")
        except Exception as e:
            print(f"Error sending completion message: {e}")
        IS_BROADCASTING = False

# Optionally, add an auto_clean task if you want to periodically update admin lists or similar
async def auto_clean():
    while not await asyncio.sleep(10):
        try:
            # Example: update configs or clean up, adapt as needed
            pass
        except Exception:
            continue
