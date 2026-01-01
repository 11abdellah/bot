import asyncio
from telethon import TelegramClient

API_ID = 30581605
API_HASH = "9f831b4169d96be5676e843bc9ee7db5"

TARGET_CHAT = -1003470822099  # قناتك

async def main():
    client = TelegramClient("test_session", API_ID, API_HASH)
    await client.start()
    await client.send_message(TARGET_CHAT, "✅ اختبار ناجح: البوت يرسل بشكل صحيح")
    print("تم الإرسال بنجاح")
    await client.disconnect()

asyncio.run(main())
