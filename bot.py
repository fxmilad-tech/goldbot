import os
import asyncio
from telethon import TelegramClient

API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

SOURCE_CHANNEL = "@mrgif"
TARGET_CHANNEL = "@PoolGoldGallery"

FOOTER_TEXT = """
✨️ گالری طلاپول ✨️   
📞 تلفن: [02144582619](tel:02144582619)
📞 تلفن: [02144585619](tel:02144585619)

بله: [Poolgold](https://ble.ir/Poolgold)
تلگرام: [PoolGoldGallery](https://t.me/PoolGoldGallery)
اینستاگرام: [poolgoldgallery](https://www.instagram.com/poolgoldgallery)

📍 آدرس: تهرانسر، خیابان ۲۲، پاساژ طلا و جواهر امیر، طلای الی (طلاپول)
"""

STATE_FILE = "last_id.txt"

async def main():
    client = TelegramClient("gold_userbot_session", API_ID, API_HASH)
    await client.start()

    # خواندن آخرین آیدی پردازش شده
    last_id = 0
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                last_id = int(f.read().strip())
        except:
            last_id = 0

    # بررسی پیام‌های جدید کانال مبدأ
    new_last_id = last_id
    async for message in client.iter_messages(SOURCE_CHANNEL, limit=5):
        if message.id > last_id:
            original_text = message.text or ""
            if original_text or message.media:
                final_text = f"{original_text}\n\n{FOOTER_TEXT}" if original_text else FOOTER_TEXT
                if message.media:
                    await client.send_file(TARGET_CHANNEL, message.media, caption=final_text, parse_mode='md')
                else:
                    await client.send_message(TARGET_CHANNEL, final_text, parse_mode='md')
            
            if message.id > new_last_id:
                new_last_id = message.id

    # ذخیره آخرین آیدی ارسال شده
    if new_last_id > last_id:
        with open(STATE_FILE, "w") as f:
            f.write(str(new_last_id))

    await client.disconnect()

asyncio.run(main())
