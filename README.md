# Text-to-Speech Converter

A small **Python text-to-speech command-line project**. It uses Google Text-to-Speech (gTTS) to generate spoken audio and `playsound` to play it.

> The current Python source converts text into speech. It does not currently implement unit, currency, temperature, or measurement conversion.

## Features

- Accepts text from a command-line argument
- Supports a language code through the `--lang` option
- Generates speech using gTTS
- Plays the generated audio
- Uses a temporary audio file in `converter2.py` and removes it after playback

## Requirements

- Python 3
- An internet connection when requesting speech from gTTS
- Audio playback support on your operating system

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Clone the repository:

```bash
git clone https://github.com/eDDie-05/Converter.git
cd Converter
```

Convert and play a phrase:

```bash
python converter2.py "Hello, welcome to my text to speech project."
```

Choose another supported gTTS language code:

```bash
python converter2.py "Bonjour tout le monde" --lang fr
```

The default language code is `en`.

## Project files

| File | Purpose |
| --- | --- |
| `converter2.py` | Command-line version with argument parsing and temporary-file cleanup |
| `converter.py` | Earlier interactive version |
| `requirements.txt` | Python dependencies |

## Current limitations

- Speech generation depends on the gTTS service and an internet connection.
- Available voices and languages depend on the speech service.
- Audio playback behavior can vary by operating system.
- The earlier `converter.py` script imports a module named `playSound`; use `converter2.py` as the documented entry point.

## Contributing

Open an issue to discuss a proposed change, then submit a focused pull request with reproduction steps.

## License

No open-source license is currently specified. All rights remain with the respective content owner unless a license is added.
