# Text to speech

Learn how to turn text into lifelike spoken audio

## Quick start

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
