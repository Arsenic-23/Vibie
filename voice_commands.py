import logging
import speech_recognition as sr
from pyrogram.types import Message

logger = logging.getLogger(__name__)

# Function to process voice commands
async def process_voice_command(message: Message):
    if not message.voice:
        return None

    file_path = await message.download()
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            command = recognizer.recognize_google(audio)
            logger.info(f"🎤 Voice Command Recognized: {command}")
            return command.lower()

    except sr.UnknownValueError:
        logger.warning("🔇 Could not understand the voice command.")
        return None
    except sr.RequestError:
        logger.error("❌ Error connecting to the voice recognition API.")
        return None