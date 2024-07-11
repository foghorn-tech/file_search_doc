# [The transcription object (Verbose JSON)](/docs/api-reference/audio/verbose-json-object)

Represents a verbose json transcription response returned by model,
based on the provided input.
| Parameter | Type | Required | Description|
| --- | --- | --- | --- |
| language | string | Optional | The language of the input audio.|
| duration | string | Optional | The duration of the input audio.|
| text | string | Optional | The transcribed text.|
| words | array | Optional | Extracted words and their corresponding timestamps.|
| segments | array | Optional | Segments of the transcribed text and their corresponding details.|

**The transcription object (Verbose JSON)**

```json
{
  "task": "transcribe",
  "language": "english",
  "duration": 8.470000267028809,
  "text": "The beach was a popular spot on a hot summer day. People were swimming in the ocean, building sandcastles, and playing beach volleyball.",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 3.319999933242798,
      "text": " The beach was a popular spot on a hot summer day.",
      "tokens": [
        50364, 440, 7534, 390, 257, 3743, 4008, 322, 257, 2368, 4266, 786, 13, 50530
      ],
      "temperature": 0.0,
      "avg_logprob": -0.2860786020755768,
      "compression_ratio": 1.2363636493682861,
      "no_speech_prob": 0.00985979475080967
    },
    ...
  ]
}
```
