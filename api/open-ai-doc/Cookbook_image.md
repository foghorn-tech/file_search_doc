# How to use the DALL·E API

This notebook shows how to use OpenAI's DALL·E image API endpoints.

There are three API endpoints:

 - Generations: generates an image or images based on an input caption
 - Edits: edits or extends an existing image
 - Variations: generates variations of an input image

## Setup

 - Import the packages you'll need
 - Import your OpenAI API key: You can do this by running `export OPENAI_API_KEY="your API key"` in your terminal.
 - Set a directory to save images to

```python
# imports
from openai import OpenAI  # OpenAI Python library to make API calls
import requests  # used to download images
import os  # used to access filepaths
from PIL import Image  # used to print and edit images

# initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))
```

```python
# set a directory to save DALL·E images to
image_dir_name = "images"
image_dir = os.path.join(os.curdir, image_dir_name)

# create the directory if it doesn't yet exist
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# print the directory to save to
print(f"{image_dir=}")
```

## Generations

The generation API endpoint creates an image based on a text prompt. API Reference

#### Required inputs:
 - `prompt` (str): A text description of the desired image(s). The maximum length is 1000 characters for dall-e-2 and 4000 characters for dall-e-3.

#### Optional inputs:

 - `model` (str): The model to use for image generation. Defaults to dall-e-2
 - n (int): The number of images to generate. Must be between 1 and 10. Defaults to 1.
 - `quality` (str): The quality of the image that will be generated. hd creates images with finer details and greater consistency across the image. This param is only supported for dall-e-3.
 - `response_format` (str): The format in which the generated images are returned. Must be one of "url" or "b64_json". Defaults to "url".
 - `size` (str): The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024 for dall-e-2. Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models. Defaults to "1024x1024".
 - `style`(str | null): The style of the generated images. Must be one of vivid or natural. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for dall-e-3.
 - `user` (str): A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. Learn more.

```python
# create an image

# set the prompt
prompt = "A cyberpunk monkey hacker dreaming of a beautiful bunch of bananas, digital art"

# call the OpenAI API
generation_response = client.images.generate(
    model = "dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024",
    response_format="url",
)

# print response
print(generation_response)
```

```python
# save the image
generated_image_name = "generated_image.png"  # any name you like; the filetype should be .png
generated_image_filepath = os.path.join(image_dir, generated_image_name)
generated_image_url = generation_response.data[0].url  # extract image URL from response
generated_image = requests.get(generated_image_url).content  # download the image

with open(generated_image_filepath, "wb") as image_file:
    image_file.write(generated_image)  # write the image to the file
```

```python
# print the image
print(generated_image_filepath)
display(Image.open(generated_image_filepath))
```