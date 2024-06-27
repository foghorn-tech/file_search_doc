# Search

Search the web using OpenAI.

```python
async def search(content: str):
    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that is trying to find the latest descriptions about a topic on Google."
            }
            {
                "role": "user",
                "content": content
            },
        ]
    )
    return completion.choices[0].message.content
```

