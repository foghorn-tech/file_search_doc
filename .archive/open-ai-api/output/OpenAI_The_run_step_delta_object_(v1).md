# [The run step delta object (v1) Legacy](/docs/api-reference/assistants-streaming-v1/run-step-delta-object)
Represents a run step delta i.e. any changed fields on a run step
          during streaming. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| id | string | Optional | The identifier of the run step, which can be referenced in API                 endpoints.| 
| object | string | Optional | The object type, which is always                 thread.run.step.delta.| 
| delta | object | Optional | The delta containing the fields that have changed on the run                 step.| 

**The run step delta object (v1)**
```python
{
  "id": "step_123",
  "object": "thread.run.step.delta",
  "delta": {
    "step_details": {
      "type": "tool_calls",
      "tool_calls": [
        {
          "index": 0,
          "id": "call_123",
          "type": "code_interpreter",
          "code_interpreter": { "input": "", "outputs": [] }
        }
      ]
    }
  }
}
```
