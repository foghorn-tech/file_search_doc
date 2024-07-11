# Input and output logs of Code Interpreter

By listing the steps of a Run that called Code Interpreter, you can inspect the code input and outputs logs of Code Interpreter:
```python
run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)
```
```json
{
  "object": "list",
  "data": [
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "type": "tool_calls",
      "run_id": "run_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "step_details": {
        "type": "tool_calls",
        "tool_calls": [
          {
            "type": "code",
            "code": {
              "input": "# Calculating 2 + 2\nresult = 2 + 2\nresult",
              "outputs": [
                {
                  "type": "logs",
                  "logs": "4"
                }
                        ...
 }
 ```