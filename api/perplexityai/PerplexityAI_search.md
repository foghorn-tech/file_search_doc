# Search By Perplexity

Send the API key as a bearer token in the Authorization header with each pplx-api request.

When you run out of credits, your API keys will be blocked until you add to your credit balance. You can avoid this by configuring "Automatic Top Up", which refreshes your balance whenever you drop below $2.

Our supported models are listed on the "Supported Models" page. The API is conveniently OpenAI client-compatible for easy integration with existing applications.

```python
from openai import OpenAI

YOUR_API_KEY = "INSERT API KEY HERE"

messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role": "user",
        "content": (
            "How many stars are in the universe?"
        ),
    },
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
response = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
)
print(response)

# chat completion with streaming
response_stream = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
    stream=True,
)
for response in response_stream:
    print(response)
```