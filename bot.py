import discord
import requests
import os

TOKEN = os.getenv("TOKEN")

LIBRE_URL = "http://localhost:5000"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def translate(text, target):
    res = requests.post(f"{LIBRE_URL}/translate", json={
        "q": text,
        "source": "auto",
        "target": target,
        "format": "text"
    })
    return res.json()["translatedText"]

@client.event
async def on_message(message):
    if message.author.bot:
        return

    text = message.content.strip()
    if not text:
        return

    output = []
    output.append(f"{message.author.display_name}: {text}")

    try:
        ja = translate(text, "ja")
        en = translate(text, "en")

        if text != ja:
            output.append(f"→ [ja] {ja}")
        if text != en:
            output.append(f"→ [en] {en}")

    except:
        output.append("→ 翻訳エラー")

    await message.channel.send("\n".join(output))

client.run(TOKEN)
