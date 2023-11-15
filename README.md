# Telegram Text-to-Speech Bot

## Overview
This Python script implements a Telegram bot that converts text to speech (TTS) and sends the audio output to users via Telegram. It utilizes the aiogram library for interacting with the Telegram Bot API and the elevenlabs library for text-to-speech conversion.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- aiogram library (`pip install aiogram`)
- elevenlabs library (Make sure you have the appropriate setup or installation method for elevenlabs)

## Setup
1. Replace `YOUR_BOT_TOKEN` in the code with your actual Telegram bot token obtained from BotFather.

2. Run the Python script `tts_bot.py`.

## Usage
- Start the bot by sending `/start` to activate it.
- Use the `/tts` command followed by the text you want to convert to speech. For example: `/tts Hello, how are you?`
- The bot will reply with an audio file containing the speech generated from the provided text.

## Implementation Details
- `/start` command: Initializes the bot and provides the user with instructions on how to use the text-to-speech functionality.
- `/tts` command: Triggers the text-to-speech conversion. The text following the command is converted to speech using the specified voice and model from the elevenlabs library.
- The generated audio file is temporarily saved as "tts_audio.ogg" and sent as a Telegram audio message to the user.
- The temporary audio file is then removed after it's sent to the user to avoid cluttering the system.

## Important Note
Ensure the elevenlabs library and its necessary components are properly configured and set up according to your environment for successful text-to-speech conversion.


