from pyrogram import Client, filters
import os

@Client.on_message(filters.command("chipmunk"))
async def chipmunk_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/chipmunk` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    output_path = file_path.replace(".mp3", "_chipmunk.mp3")

    os.system(f"ffmpeg -i {file_path} -af asetrate=44100*1.5,atempo=0.8 {output_path}")

    await message.reply_audio(audio=output_path, caption="🐿️ Chipmunk Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)

@Client.on_message(filters.command("deep"))
async def deep_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/deep` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    output_path = file_path.replace(".mp3", "_deep.mp3")

    os.system(f"ffmpeg -i {file_path} -af asetrate=44100*0.8,atempo=1.25 {output_path}")

    await message.reply_audio(audio=output_path, caption="🎶 Deep Voice Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)

@Client.on_message(filters.command("echo"))
async def echo_effect(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        return await message.reply_text("🎵 Reply to an audio file with `/echo` to apply the effect.")

    file_path = await client.download_media(message.reply_to_message)
    output_path = file_path.replace(".mp3", "_echo.mp3")

    os.system(f"ffmpeg -i {file_path} -af aecho=0.8:0.88:60:0.4 {output_path}")

    await message.reply_audio(audio=output_path, caption="🔊 Echo Effect Applied!")
    os.remove(file_path)
    os.remove(output_path)
