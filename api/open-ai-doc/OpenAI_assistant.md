# How to create Assistant

## Step 1: Create an Assistant

```python
from openai import OpenAI
client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)
```

## Step 2: Create a Thread

```python
thread = client.beta.threads.create()
```

## Step 3: Add a Message to the Thread

User or app-generated messages, with text and files, become Message objects in the Thread. Messages are unlimited; context is smartly truncated to fit the model's window.

```python
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
```

## Step 4: Create a Run
After adding all user messages to the Thread, you can initiate a Run with any Assistant. A Run leverages the model and tools to produce responses, which are then appended as assistant Messages to the Thread.

```python
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)
```

Once the Run completes, you can list the Messages added to the Thread by the Assistant.

```python
if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages.data[0].content[0].text.value)
else:
  print(run.status)

```
You may also want to list the Run Steps of this Run if you'd like to look at any tool calls made during this Run.