# Speech to text

Learn how to turn audio into text

## Transcriptions

```python
from openai import OpenAI
client = OpenAI()

audio_file= open("/path/to/file/audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
print(transcription.text)
```

The Audio API also allows you to set additional parameters in a request. For example, if you want to set the response_format as text, your request would look like the following:

```python
from openai import OpenAI
client = OpenAI()

audio_file = open("/path/to/file/speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)
print(transcription)
```

## Translations

The translations API takes as input the audio file in any of the supported languages and transcribes, if necessary, the audio into English. This differs from our /Transcriptions endpoint since the output is not in the original input language and is instead translated to English text.

Translate audio

```python
from openai import OpenAI
client = OpenAI()

audio_file= open("/path/to/file/german.mp3", "rb")
translation = client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)
print(translation.text)
```

## Supported languages

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

## Timestamps

By default, the Whisper API will output a transcript of the provided audio in text. The timestamp_granularities[] parameter enables a more structured and timestamped json output format, with timestamps at the segment, word level, or both. This enables word-level precision for transcripts and video edits, which allows for the removal of specific frames tied to individual words.

Timestamp options

```python
from openai import OpenAI
client = OpenAI()

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
file=audio_file,
model="whisper-1",
response_format="verbose_json",
timestamp_granularities=["word"]
)

print(transcript.words)
```
