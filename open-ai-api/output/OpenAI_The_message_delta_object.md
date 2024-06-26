# [The message delta object Beta](/docs/api-reference/assistants-streaming/message-delta-object)
Represents a message delta i.e. any changed fields on a message during
          streaming. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier of the message, which can be referenced in API                 endpoints.| 
| object | string | Optional | The object type, which is always                 thread.message.delta.| 
| delta | object | Optional | The delta containing the fields that have changed on the                 Message.| 

**The message delta object**
```python
{
  "id": "msg_123",
  "object": "thread.message.delta",
  "delta": {
    "content": [
      {
        "index": 0,
        "type": "text",
        "text": { "value": "Hello", "annotations": [] }
      }
    ]
  }
}
```
