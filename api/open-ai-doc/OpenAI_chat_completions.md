# Chat Completions API

## Overview

The Chat Completions API supports text and image inputs, and can output text content (including code and JSON).

It accepts inputs via the messages parameter, which is an array of message objects.

## Message roles

Each message object has a role (either system, user, or assistant) and content.

The system message is optional and can be used to set the behavior of the assistant
The user messages provide requests or comments for the assistant to respond to
Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behavior (few-shot examples)

## Quick start

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
```

## Chat Completions response format

```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
      "logprobs": null
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
```

The assistant's reply can be extracted with:

```python
message = completion.choices[0].message.content
```

