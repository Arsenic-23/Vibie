import os
import subprocess
from pyrogram import Client, filters

@Client.on_message(filters.command("chipmunk"))
async def chipmunk_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/chipmunk` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    base_name, ext = os.path.splitext(file_path)
    output_path = f"{base_name}_chipmunk{ext}"

    subprocess.run(["ffmpeg", "-i", file_path, "-af", "asetrate=44100*1.5,atempo=0.8", output_path])

    await message.reply_audio(audio=output_path, caption="🐿️ Chipmunk Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)

@Client.on_message(filters.command("deep"))
async def deep_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/deep` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    base_name, ext = os.path.splitext(file_path)
    output_path = f"{base_name}_deep{ext}"

    subprocess.run(["ffmpeg", "-i", file_path, "-af", "asetrate=44100*0.8,atempo=1.25", output_path])

    await message.reply_audio(audio=output_path, caption="🎶 Deep Voice Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)

@Client.on_message(filters.command("echo"))
async def echo_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/echo` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    base_name, ext = os.path.splitext(file_path)
    output_path = f"{base_name}_echo{ext}"

    subprocess.run(["ffmpeg", "-i", file_path, "-af", "aecho=0.8:0.88:60:0.4", output_path])

    await message.reply_audio(audio=output_path, caption="🔊 Echo Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)

# Export handlers for main.py
handlers = [chipmunk_effect, deep_effect, echo_effect]