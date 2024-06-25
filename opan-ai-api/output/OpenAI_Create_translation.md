# [Create translation](/docs/api-reference/audio/createTranslation)
post https://api.openai.com/v1/audio/translations 
Translates audio into English. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file | file | Required | The audio file object (not file name) translate, in one of                   these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or                   webm.| 
| model | string | Required | ID of the model to use. Only whisper-1 (which is                   powered by our open source Whisper V2 model) is currently                   available.| 
| prompt | string | Optional | An optional text to guide the model's style or continue a                   previous audio segment. The                   prompt                   should be in English.| 
| response_format | string | Optional | The format of the transcript output, in one of these options:                   json, text, srt,                   verbose_json, or vtt.| 
| temperature | number | Optional | The sampling temperature, between 0 and 1. Higher values like                   0.8 will make the output more random, while lower values like                   0.2 will make it more focused and deterministic. If set to 0,                   the model will use                   log probability                   to automatically increase the temperature until certain                   thresholds are hit.| 
## Returns 
The translated text. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
audio_file = open("speech.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)
```

**Response**
```python
{
  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
}
```
