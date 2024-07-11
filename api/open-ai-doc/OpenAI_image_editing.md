# Image generation

Learn how to manipulate images with DALL·E in the openai API.

## Usage

## Edits (DALL·E 2 only)

Also known as "inpainting", the image edits endpoint allows you to edit or extend an image by uploading an image and mask indicating which areas should be replaced. The transparent areas of the mask indicate where the image should be edited, and the prompt should describe the full new image, *not just the erased area*. This endpoint can enable experiences like DALL·E image editing in ChatGPT Plus.

```python
from openai import OpenAI
client = OpenAI()

response = client.images.edit(
  model="dall-e-2",
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url
```

The uploaded image and mask must both be square PNG images less than 4MB in size, and also must have the same dimensions as each other. The non-transparent areas of the mask are not used when generating the output, so they don’t necessarily need to match the original image like the example above.

## Variations (DALL·E 2 only)
The image variations endpoint allows you to generate a variation of a given image.

```python
from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
  model="dall-e-2",
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
```

Similar to the edits endpoint, the input image must be a square PNG image less than 4MB in size.
