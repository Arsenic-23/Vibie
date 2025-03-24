from pyrogram import Client, filters
import os

# Dictionary mapping effect names to FFmpeg filters
AUDIO_EFFECTS = {
    "chipmunk": "asetrate=44100*1.5,atempo=0.8",
    "deep": "asetrate=44100*0.8,atempo=1.25",
    "echo": "aecho=0.8:0.88:6:0.4",
    "robot": "afftfilt='real='if(gt(fmod(N,16),8),-1,1)':imag=0'",
}

@Client.on_message(filters.command(["effect"]) & filters.reply)
async def apply_effect(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/effect <chipmunk/deep/echo/robot>` (reply to an audio file)")

    effect = message.command[1].lower()
    if effect not in AUDIO_EFFECTS:
        return await message.reply_text("Invalid effect. Choose from: chipmunk, deep, echo, robot.")

    replied = message.reply_to_message
    if not replied.audio and not replied.voice:
        return await message.reply_text("Please reply to an audio file or voice note.")

    audio_file = await replied.download()
    output_file = f"processed_{effect}.ogg"

    # Apply effect using FFmpeg
    os.system(f"ffmpeg -i {audio_file} -af \"{AUDIO_EFFECTS[effect]}\" {output_file}")

    # Send the processed audio
    await message.reply_audio(output_file, caption=f"Here is your `{effect}` effect! 🎵")

    # Clean up files
    os.remove(audio_file)
    os.remove(output_file)