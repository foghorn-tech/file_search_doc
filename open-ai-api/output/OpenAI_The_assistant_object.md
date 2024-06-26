# [The assistant object Beta](/docs/api-reference/assistants/object)
Represents an assistant that can call the model and use
          tools. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier, which can be referenced in API endpoints.| 
| object | string | Optional | The object type, which is always assistant.| 
| created_at | integer | Optional | The Unix timestamp (in seconds) for when the assistant was                 created.| 
| name | string or null | Optional | The name of the assistant. The maximum length is 256 characters.| 
| description | string or null | Optional | The description of the assistant. The maximum length is 512                 characters.| 
| model | string | Optional | ID of the model to use. You can use the                 List models API to                 see all of your available models, or see our                 Model overview for                 descriptions of them.| 
| instructions | string or null | Optional | The system instructions that the assistant uses. The maximum                 length is 256,000 characters.| 
| tools | array | Optional | A list of tool enabled on the assistant. There can be a maximum                 of 128 tools per assistant. Tools can be of types                 code_interpreter, file_search, or                 function.| 
| tool_resources | object or null | Optional | A set of resources that are used by the assistant's tools. The                 resources are specific to the type of tool. For example, the                 code_interpreter tool requires a list of file IDs,                 while the file_search tool requires a list of                 vector store IDs.| 
| metadata | map | Optional | Set of 16 key-value pairs that can be attached to an object.                 This can be useful for storing additional information about the                 object in a structured format. Keys can be a maximum of 64                 characters long and values can be a maxium of 512 characters                 long.| 
| temperature | number or null | Optional | What sampling temperature to use, between 0 and 2. Higher values                 like 0.8 will make the output more random, while lower values                 like 0.2 will make it more focused and deterministic.| 
| top_p | number or null | Optional | An alternative to sampling with temperature, called nucleus                 sampling, where the model considers the results of the tokens                 with top_p probability mass. So 0.1 means only the tokens                 comprising the top 10% probability mass are considered.                                 We generally recommend altering this or temperature but not                 both.| 
| response_format | string or object | Optional | Specifies the format that the model must output. Compatible with                 GPT-4o,                 GPT-4 Turbo,                 and all GPT-3.5 Turbo models since                 gpt-3.5-turbo-1106.                                 Setting to { "type": "json_object" } enables JSON                 mode, which guarantees the message the model generates is valid                 JSON.                 Important: when using JSON mode, you                 must also instruct the model to produce JSON                 yourself via a system or user message. Without this, the model                 may generate an unending stream of whitespace until the                 generation reaches the token limit, resulting in a long-running                 and seemingly "stuck" request. Also note that the message                 content may be partially cut off if                 finish_reason="length", which indicates the                 generation exceeded max_tokens or the conversation                 exceeded the max context length.| 

**The assistant object**
```python
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4-turbo",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "metadata": {},
  "top_p": 1.0,
  "temperature": 1.0,
  "response_format": "auto"
}
```
