from telethon import TelegramClient, events

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

client = TelegramClient("gold_userbot_session", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_and_modify(event):
    original_text = event.message.text or ""
    if original_text:
        final_text = f"{original_text}\n\n{FOOTER_TEXT}"
        if event.message.media:
            await client.send_file(TARGET_CHANNEL, event.message.media, caption=final_text, parse_mode='md')
        else:
            await client.send_message(TARGET_CHANNEL, final_text, parse_mode='md')

print("🤖 یوزربات طلا پول روشن شد...")
client.start()
client.run_until_disconnected()
