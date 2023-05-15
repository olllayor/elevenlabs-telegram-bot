import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
from elevenlabs import generate, play
from config import token
# Replace YOUR_BOT_TOKEN with your Telegram bot token
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # Create a keyboard with a single "TTS" button
    tts_button = types.KeyboardButton("/tts")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(tts_button)
    
    # Send a welcome message with instructions and the TTS button to the user
    welcome_message = "Hi! I'm a text-to-speech bot. Press the TTS button to convert text to speech!"
    await message.answer(welcome_message, reply_markup=keyboard)


@dp.message_handler(commands=['tts'])
async def tts_handler(message: types.Message):
    # Get the text to be converted to speech from the user's message
    text = message.text[4:]
    
    # Set the voice to use for text-to-speech. Default is "Bella"
    voice = "Adam"
    
    # Set the model to use for text-to-speech. Default is "eleven_monolingual_v1"
    model = "eleven_monolingual_v1"
    
    # Generate the audio data using the elevenlabs library
    audio_data = generate(text=text, voice=voice, model=model)
    
    # Save the audio data to a temporary file
    with open("tts_audio.ogg", "wb") as f:
        f.write(audio_data)
    
    # Send the audio file to the user
    audio_file = types.InputFile("tts_audio.ogg")
    await message.answer_audio(audio_file)

    # Remove the temporary audio file
    os.remove("tts_audio.ogg")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
