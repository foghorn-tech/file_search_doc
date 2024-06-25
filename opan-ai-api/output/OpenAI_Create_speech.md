# [Create speech](/docs/api-reference/audio/createSpeech)
post https://api.openai.com/v1/audio/speech 
Generates audio from the input text. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| model | string | Required | One of the available                   TTS models:                   tts-1 or tts-1-hd| 
| input | string | Required | The text to generate audio for. The maximum length is 4096                   characters.| 
| voice | string | Required | The voice to use when generating the audio. Supported voices                   are alloy, echo, fable,                   onyx, nova, and                   shimmer. Previews of the voices are available in                   the                   Text to speech guide.| 
| response_format | string | Optional | The format to audio in. Supported formats are                   mp3, opus, aac,                   flac, wav, and pcm.| 
| speed | number | Optional | The speed of the generated audio. Select a value from                   0.25 to 4.0. 1.0 is the                   default.| 
## Returns 
The audio file content. 

**Example request**
```python
from pathlib import Pathimport openaispeech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)
```
