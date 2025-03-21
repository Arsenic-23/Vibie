from pyrogram import Client, filters
import subprocess

# Function to apply Chipmunk effect using FFmpeg
def apply_chipmunk_effect(input_audio: str, output_audio: str):
    """Apply chipmunk effect using FFmpeg"""
    try:
        # FFmpeg command to apply the chipmunk effect (speed up the audio)
        ffmpeg_command = [
            "ffmpeg",
            "-i", input_audio,  # Input file
            "-filter:a", "atempo=1.5,asetrate=44100*1.5",  # Chipmunk effect
            "-vn",  # No video
            output_audio  # Output file
        ]
        subprocess.run(ffmpeg_command, check=True)
        print(f"✅ Chipmunk effect applied to {input_audio} successfully!")
        return output_audio
    except Exception as e:
        print(f"❌ Failed to apply chipmunk effect: {e}")
        return None

# Register handlers
def register_handlers(app: Client):
    @app.on_message(filters.command("chipmunk") & filters.group)
    async def chipmunk_effect(client, message):
        chat_id = message.chat.id
        if message.reply_to_message and message.reply_to_message.audio:
            audio_file = message.reply_to_message.audio.file_id
            # Download the audio file to apply the effect
            downloaded_file = await client.download_media(audio_file)
            output_file = "output_chipmunk_audio.mp3"  # Temporary output file

            # Apply the chipmunk effect using FFmpeg
            result = apply_chipmunk_effect(downloaded_file, output_file)

            if result:
                # Send the processed audio file with the chipmunk effect applied
                await message.reply_audio(output_file, caption="🐿️ **Chipmunk effect applied!**")
                # Optionally delete temporary files after sending
                os.remove(downloaded_file)
                os.remove(output_file)
            else:
                await message.reply_text("❌ Failed to apply chipmunk effect!")
        else:
            await message.reply_text("❗ Please reply to an audio message to apply the effect.")