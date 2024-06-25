# [Assistant stream events Beta](/docs/api-reference/assistants-streaming/events)
Represents an event emitted when streaming a Run. 
Each event in a server-sent events stream has an
          event and data property: 

```python
event: thread.created
data: {"id": "thread_123", "object": "thread", ...}
```
We emit events whenever a new object is created, transitions to a new
          state, or is being streamed in parts (deltas). For example, we emit
          thread.run.created when a new run is created,
          thread.run.completed when a run completes, and so on.
          When an Assistant chooses to create a message during a run, we emit a
          thread.message.created event, a
          thread.message.in_progress event, many
          thread.message.delta events, and finally a
          thread.message.completed event. 
We may add additional events over time, so we recommend handling
          unknown events gracefully in your code. See the
          [Assistants API quickstart](/docs/assistants/overview) to
          learn how to integrate the Assistants API with streaming. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| thread.created | data is a                   thread | Optional | Occurs when a new                 thread is                 created.| 
| thread.run.created | data is a                   run | Optional | Occurs when a new                 run is created.| 
| thread.run.queued | data is a                   run | Optional | Occurs when a                 run moves to a                 queued status.| 
| thread.run.in_progress | data is a                   run | Optional | Occurs when a                 run moves to an                 in_progress status.| 
| thread.run.requires_action | data is a                   run | Optional | Occurs when a                 run moves to a                 requires_action status.| 
| thread.run.completed | data is a                   run | Optional | Occurs when a                 run is completed.| 
| thread.run.incomplete | data is a                   run | Optional | Occurs when a                 run ends with                 status incomplete.| 
| thread.run.failed | data is a                   run | Optional | Occurs when a                 run fails.| 
| thread.run.cancelling | data is a                   run | Optional | Occurs when a                 run moves to a                 cancelling status.| 
| thread.run.cancelled | data is a                   run | Optional | Occurs when a                 run is cancelled.| 
| thread.run.expired | data is a                   run | Optional | Occurs when a                 run expires.| 
| thread.run.step.created | data is a                   run step | Optional | Occurs when a                 run step is                 created.| 
| thread.run.step.in_progress | data is a                   run step | Optional | Occurs when a                 run step                 moves to an in_progress state.| 
| thread.run.step.delta | data is a                   run step delta | Optional | Occurs when parts of a                 run step are                 being streamed.| 
| thread.run.step.completed | data is a                   run step | Optional | Occurs when a                 run step is                 completed.| 
| thread.run.step.failed | data is a                   run step | Optional | Occurs when a                 run step                 fails.| 
| thread.run.step.cancelled | data is a                   run step | Optional | Occurs when a                 run step is                 cancelled.| 
| thread.run.step.expired | data is a                   run step | Optional | Occurs when a                 run step                 expires.| 
| thread.message.created | data is a                   message | Optional | Occurs when a                 message is                 created.| 
| thread.message.in_progress | data is a                   message | Optional | Occurs when a                 message moves                 to an in_progress state.| 
| thread.message.delta | data is a                   message delta | Optional | Occurs when parts of a                 Message are                 being streamed.| 
| thread.message.completed | data is a                   message | Optional | Occurs when a                 message is                 completed.| 
| thread.message.incomplete | data is a                   message | Optional | Occurs when a                 message ends                 before it is completed.| 
| error | data is an                   error | Optional | Occurs when an                 error occurs.                 This can happen due to an internal server error or a timeout.| 
| done | data is [DONE] | Optional | Occurs when a stream ends.| 
