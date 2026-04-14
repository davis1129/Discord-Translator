import discord
from googletrans import Translator
import os

TOKEN = os.getenv("TOKEN")

translator = Translator()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    text = message.content.strip()
    if not text:
        return

    output = []

    try:
        ja = translator.translate(text, dest="ja").text
        en = translator.translate(text, dest="en").text

        if text != ja:
            output.append(f"[ja] {ja}")
        if text != en:
            output.append(f"[en] {en}")

    except:
        output.append("※ 翻訳エラー（Translation error）")

    await message.channel.send("\n".join(output))

client.run(TOKEN)
