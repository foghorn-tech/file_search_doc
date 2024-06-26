# [Training format for chat models](/docs/api-reference/fine-tuning/chat-input)
The per-line training example of a fine-tuning input file for chat
          models 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| messages | array | Optional | | 
| tools | array | Optional | A list of tools the model may generate JSON inputs for.| 
| parallel_tool_calls | boolean | Optional | Whether to enable                 parallel function calling                 during tool use.| 
| functions | array | Optional | A list of functions the model may generate JSON inputs for.| 

**Training format for chat models**
```python
{
  "messages": [
    { "role": "user", "content": "What is the weather in San Francisco?" },
    {
      "role": "assistant",
      "tool_calls": [
        {
          "id": "call_id",
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "arguments": "{\"location\": \"San Francisco, USA\", \"format\": \"celsius\"}"
          }
        }
      ]
    }
  ],
  "parallel_tool_calls": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, eg. San Francisco, USA"
            },
            "format": { "type": "string", "enum": ["celsius", "fahrenheit"] }
          },
          "required": ["location", "format"]
        }
      }
    }
  ]
}
```
