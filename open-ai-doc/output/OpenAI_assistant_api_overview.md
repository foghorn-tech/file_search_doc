# OpenAI Assistant API Overview

## Chat Completions API vs Assistants API

The primitives of the Chat Completions API are Messages, on which you perform a Completion with a Model (gpt-3.5-turbo, gpt-4, etc). It is lightweight and powerful, but inherently stateless, which means you have to manage conversation state, tool definitions, retrieval documents, and code execution manually.

The primitives of the Assistants API are

Assistants, which encapsulate a base model, instructions, tools, and (context) documents,
Threads, which represent the state of a conversation, and
Runs, which power the execution of an Assistant on a Thread, including textual responses and multi-step tool use.
We'll take a look at how these can be used to create powerful, stateful experiences.

## How to create Assistant

### Step 1: Create an Assistant

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less.",
    model="gpt-4-1106-preview",
)
show_json(assistant)
```

```json
{'id': 'asst_9HAjl9y41ufsViNcThW1EXUS',
 'created_at': 1699828331,
 'description': None,
 'file_ids': [],
 'instructions': 'You are a personal math tutor. Answer questions briefly, in a sentence or less.',
 'metadata': {},
 'model': 'gpt-4-1106-preview',
 'name': 'Math Tutor',
 'object': 'assistant',
 'tools': []}
```

### Step 2: Create a Thread

```python
thread = client.beta.threads.create()
show_json(thread)
```

```json
{'id': 'thrd_9HAjv1y41ufsViNcThW1EXUS',
 'created_at': 1699828331,
 'object': 'thread'}
```

### Step 3: Add a Message to the Thread

```python
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the square root of 16?"
)
show_json(message)
```

```json
{'id': 'msg_9HAjw1y41ufsViNcThW1EXUS',
 'content': 'What is the square root of 16?',
 'created_at': 1699828331,
 'object': 'message',
 'role': 'user',
 'thread_id': 'thrd_9HAjv1y41ufsViNcThW1EXUS'}
```

### Step 4: Create a Run

```python
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
show_json(run)
```

```json
{'id': 'run_LA08RjouV3RemQ78UZXuyzv6',
 'assistant_id': 'asst_9HAjl9y41ufsViNcThW1EXUS',
 'cancelled_at': None,
 'completed_at': None,
 'created_at': 1699828332,
 'expires_at': 1699828932,
 'failed_at': None,
 'file_ids': [],
 'instructions': 'You are a personal math tutor. Answer questions briefly, in a sentence or less.',
 'last_error': None,
 'metadata': {},
 'model': 'gpt-4-1106-preview',
 'object': 'thread.run',
 'required_action': None,
 'started_at': None,
 'status': 'queued',
 'thread_id': 'thread_bw42vPoQtYBMQE84WubNcJXG',
 'tools': []}
```

### Step 5: Poll for completion

```python

