#!/usr/bin/env python3
import argparse
import os
import tempfile

from gtts import gTTS
from playsound import playsound


def text_to_speech_and_play(text: str, lang: str = "en") -> None:
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_path = temp_audio.name

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(temp_path)
        playsound(temp_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert text to speech with gTTS and play it with playsound."
    )
    parser.add_argument("text", help="Text to convert to speech.")
    parser.add_argument(
        "--lang",
        default="en",
        help="Language code for gTTS (default: en). Example: en, hi, fr",
    )
    args = parser.parse_args()

    text_to_speech_and_play(args.text, args.lang)


if __name__ == "__main__":
    main()