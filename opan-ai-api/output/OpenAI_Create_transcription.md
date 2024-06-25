# [Create transcription](/docs/api-reference/audio/createTranscription)
post https://api.openai.com/v1/audio/transcriptions 
Transcribes audio into the input language. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| file | file | Required | The audio file object (not file name) to transcribe, in one of                   these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or                   webm.| 
| model | string | Required | ID of the model to use. Only whisper-1 (which is                   powered by our open source Whisper V2 model) is currently                   available.| 
| language | string | Optional | The language of the input audio. Supplying the input language                   in                   ISO-639-1                   format will improve accuracy and latency.| 
| prompt | string | Optional | An optional text to guide the model's style or continue a                   previous audio segment. The                   prompt                   should match the audio language.| 
| response_format | string | Optional | The format of the transcript output, in one of these options:                   json, text, srt,                   verbose_json, or vtt.| 
| temperature | number | Optional | The sampling temperature, between 0 and 1. Higher values like                   0.8 will make the output more random, while lower values like                   0.2 will make it more focused and deterministic. If set to 0,                   the model will use                   log probability                   to automatically increase the temperature until certain                   thresholds are hit.| 
| timestamp_granularities[] | array | Optional | The timestamp granularities to populate for this                   transcription. response_format must be set                   verbose_json to use timestamp granularities.                   Either or both of these options are supported:                   word, or segment. Note: There is no                   additional latency for segment timestamps, but generating word                   timestamps incurs additional latency.| 
## Returns 
The
                [transcription object](/docs/api-reference/audio/json-object)
                or a
                verbose [transcription object](/docs/api-reference/audio/json-object). 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
```

**Response**
```python
{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
}
```
