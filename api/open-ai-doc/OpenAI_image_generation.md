# Image generation

Learn how to use ai to *generate images from texts* with the openai API.

## Usage

### Generations

By default, images are generated at `standard` quality, but when using DALL·E 3 you can set `quality: "hd"` for enhanced detail. Square, standard quality images are the fastest to generate.

```python
from openai import OpenAI

client = OpenAI(
  api_key=YOUR_API_KEY,
)

# Any prompt you like, for example:
prompt = "a white siamese cat"

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
```

### Deprecated usage

`openai.Image` is no longer supported by openai anymore. using it will caused an "APIRemovedv1" error.

openai.Image.create() -> client.images.generate()
openai.Image.create_variation() -> client.images.create_variation()
openai.Image.create_edit() -> client.images.edit()
