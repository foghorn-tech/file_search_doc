# Code interpreter

## Get Code interpreter Result

```python
run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=my_assistant.id)
if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print(run.status)
```