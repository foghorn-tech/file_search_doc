# Text to speech

Learn how to turn text into lifelike spoken audio

## Quick start

The speech endpoint takes in three key inputs:

- the model
- the text that should be turned into audio
- the voice to be used for the audio generation.

A simple request would look like the following:

```python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
```

By default, the endpoint will output a MP3 file of the spoken audio but it can also be configured to output any of our supported formats like "opus", "aac", "flac", and "pcm" are available.

## Voice options

The current voices are optimized for English.

- Alloy
- Echo
- Fable
- Onyx
- Nova
- Shimmer

## Supported output formats

The default response format is "mp3", but other formats like "opus", "aac", "flac", and "pcm" are available.

- Opus: For internet streaming and communication, low latency.
- AAC: For digital audio compression, preferred by YouTube, Android, iOS.
- FLAC: For lossless audio compression, favored by audio enthusiasts for archiving.
- WAV: Uncompressed WAV audio, suitable for low-latency applications to avoid decoding overhead.
- PCM: Similar to WAV but containing the raw samples in 24kHz (16-bit signed, low-endian), without the header.

## Supported languages

The TTS model generally follows the Whisper model in terms of language support. Whisper supports the following languages and performs well despite the current voices being optimized for English:

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

You can generate spoken audio in these languages by providing the input text in the language of your choice.
