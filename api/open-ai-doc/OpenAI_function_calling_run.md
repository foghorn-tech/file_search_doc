# How to run function calling

## Step 1: Create a Thread and add Messages
```python
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What's the weather in San Francisco today?",
)
```

## Step 2: Initiate a Run
```python

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
     print(messages.data[0].content[0].text.value)
else:
    print(run.status)

# Define the list to store tool outputs
tool_outputs = []

# Loop through each tool in the required action section
for tool in run.required_action.submit_tool_outputs.tool_calls:
    if tool.function.name == "get_current_temperature":
        args = json.loads(tool.function.arguments)
        tool_outputs.append(
            {
                "tool_call_id": tool.id,
                "output": get_current_temperature(**args)
            }
        )

if tool_outputs:
    try:
        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
        print("Submitted successfully.")
    except Exception as e:
        print("Failed to submit:", e)
else:
    print("No outputs to submit.")

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages.data[0].content[0].text.value)
else:
    print(run.status)
```