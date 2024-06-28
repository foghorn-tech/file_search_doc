# Build a basic LLM chat app

Before we start building, let's take a closer look at the chat elements we'll use.

## Chat elements

### st.chat_message
st.chat_message lets you insert a multi-element chat message container into your app. The returned container can contain any Streamlit element, including charts, tables, text, and more. To add elements to the returned container, you can use with notation.

st.chat_message's first parameter is the name of the message author, which can be either "user" or "assistant" to enable preset styling and avatars, like in the demo above. You can also pass in a custom string to use as the author name. Currently, the name is not shown in the UI but is only set as an accessibility label. For accessibility reasons, you should not use an empty string.

Here's an minimal example of how to use st.chat_message to display a welcome message:

```python
import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")

```

Notice the message is displayed with a default avatar and styling since we passed in "user" as the author name. You can also pass in "assistant" as the author name to use a different default avatar and styling, or pass in a custom name and avatar. See the API reference for more details.
```python
import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))

```

While we've used the preferred with notation in the above examples, you can also just call methods directly in the returned objects. The below example is equivalent to the one above:

```python
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
```

So far, we've displayed predefined messages. But what if we want to display messages based on user input?


### st.chat_input
st.chat_input lets you display a chat input widget so the user can type in a message. The returned value is the user's input, which is None if the user hasn't sent a message yet. You can also pass in a default prompt to display in the input widget. Here's an example of how to use st.chat_input to display a chat input widget and show the user's input:

```python
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

```


## Build a simple chatbot GUI with streaming
In this section, we'll build a simple chatbot GUI that responds to user input with a random message from a list of pre-determind responses. In the next section, we'll convert this simple toy example into a ChatGPT-like experience using OpenAI.

Just like previously, we still require the same components to build our chatbot. Two chat message containers to display messages from the user and the bot, respectively. A chat input widget so the user can type in a message. And a way to store the chat history so we can display it in the chat message containers.

Let's just copy the code from the previous section and add a few tweaks to it.

import streamlit as st
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
The only difference so far is we've changed the title of our app and added imports for random and time. We'll use random to randomly select a response from a list of responses and time to add a delay to simulate the chatbot "thinking" before responding.

All that's left to do is add the chatbot's responses within the if block. We'll use a list of responses and randomly select one to display. We'll also add a delay to simulate the chatbot "thinking" before responding (or stream its response). Let's make a helper function for this and insert it at the top of our app.

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
Back to writing the response in our chat interface, we'll use st.write_stream to write out the streamed response with a typewriter effect.

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
Above, we've added a placeholder to display the chatbot's response. We've also added a for loop to iterate through the response and display it one word at a time. We've added a delay of 0.05 seconds between each word to simulate the chatbot "thinking" before responding. Finally, we append the chatbot's response to the chat history. As you've probably guessed, this is a naive implementation of streaming. We'll see how to implement streaming with OpenAI in the next section.

Putting it all together, here's the full code for our simple chatbot GUI and the result:

View full code
expand_more

Built with Streamlit 🎈
Fullscreen
open_in_new
Play around with the above demo to get a feel for what we've built. It's a very simple chatbot GUI, but it has all the components of a more sophisticated chatbot. In the next section, we'll see how to build a ChatGPT-like app using OpenAI.

Build a ChatGPT-like app
Now that you've understood the basics of Streamlit's chat elements, let's make a few tweaks to it to build our own ChatGPT-like app. You'll need to install the OpenAI Python library and get an API key to follow along.

Install dependencies
First let's install the dependencies we'll need for this section:

pip install openai streamlit
Add OpenAI API key to Streamlit secrets
Next, let's add our OpenAI API key to Streamlit secrets. We do this by creating .streamlit/secrets.toml file in our project directory and adding the following lines to it:

# .streamlit/secrets.toml
OPENAI_API_KEY = "YOUR_API_KEY"
Write the app
Now let's write the app. We'll use the same code as before, but we'll replace the list of responses with a call to the OpenAI API. We'll also add a few more tweaks to make the app more ChatGPT-like.

import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
All that's changed is that we've added a default model to st.session_state and set our OpenAI API key from Streamlit secrets. Here's where it gets interesting. We can replace our emulated stream with the model's responses from OpenAI:

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
Above, we've replaced the list of responses with a call to OpenAI().chat.completions.create. We've set stream=True to stream the responses to the frontend. In the API call, we pass the model name we hardcoded in session state and pass the chat history as a list of messages. We also pass the role and content of each message in the chat history. Finally, OpenAI returns a stream of responses (split into chunks of tokens), which we iterate through and display each chunk.

Putting it all together, here's the full code for our ChatGPT-like app and the result:

View full code
expand_more

Built with Streamlit 🎈
Fullscreen
open_in_new
Congratulations! You've built your own ChatGPT-like app in less than 50 lines of code.

We're very excited to see what you'll build with Streamlit's chat elements. Experiment with different models and tweak the code to build your own conversational apps. If you build something cool, let us know on the Forum or check out some other Generative AI apps for inspiration. 🎈

Previous: