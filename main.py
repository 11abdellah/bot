import asyncio
import random
from telethon import TelegramClient, events

# =============================
# 1️⃣ بياناتك
# =============================
API_ID = 30581605
API_HASH = "9f831b4169d96be5676e843bc9ee7db5"

SOURCE_CHATS = [
    -1001933446347  # قناة/بوت المصدر
]

TARGET_CHAT = -1003470822099  # قناتك

AFFILIATE_LINK = "https://broker-qx.pro/sign-up/?lid=1696288"

# =============================
# 2️⃣ تشغيل العميل
# =============================
client = TelegramClient("session_abdou", API_ID, API_HASH)

print("✅ البوت يعمل الآن... في انتظار إشارات")

# =============================
# 3️⃣ التقاط الإشارات
# =============================
@client.on(events.NewMessage(chats=SOURCE_CHATS))
async def handler(event):
    text = event.raw_text.strip()
    if not text:
        return

    lower_text = text.lower()

    # =============================
    # 4️⃣ إذا كانت نتيجة (WIN / LOSS) ترسل كما هي
    # =============================
    if "win" in lower_text or "loss" in lower_text:
        await client.send_message(TARGET_CHAT, text)
        print("📤 تم إرسال النتيجة كما هي")
        return

    # =============================
    # 5️⃣ تنظيف الإشارة
    # =============================
    cleaned_lines = []
    for line in text.splitlines():
        line_lower = line.lower()

        # حذف الروابط والمنشن
        if "http" in line_lower or "@" in line_lower:
            continue

        # حذف اسم البوت المصدر
        if "eyad trader bot" in line_lower:
            continue

        if line.strip():
            cleaned_lines.append(line.strip())

    if not cleaned_lines:
        return

    clean_signal = "\n".join(cleaned_lines)

    # =============================
    # 6️⃣ تنسيق احترافي + نسبة وهمية
    # =============================
    accuracy = random.randint(88, 97)

    final_message = f"""
🚨 VIP TRADING SIGNAL 🚨

{clean_signal}

📊 Accuracy: {accuracy}%
⏱ Expiry: 1 Minute
💰 Market: OTC

🔗 Trade Here
👉 {AFFILIATE_LINK}

⚠️ Risk management required
👑 Premium Signals
"""

    await client.send_message(TARGET_CHAT, final_message.strip())
    print("📤 تم إرسال إشارة معدلة بنجاح")

# =============================
# 7️⃣ تشغيل دائم
# =============================
client.start()
client.run_until_disconnected()
