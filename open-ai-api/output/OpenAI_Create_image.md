# [Create image](/docs/api-reference/images/create)
post https://api.openai.com/v1/images/generations 
Creates an image given a prompt. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| prompt | string | Required | A text description of the desired image(s). The maximum length                   is 1000 characters for dall-e-2 and 4000                   characters for dall-e-3.| 
| model | string | Optional | The model to use for image generation.| 
| n | integer or null | Optional | The number of images to generate. Must be between 1 and 10.                   For dall-e-3, only n=1 is supported.| 
| quality | string | Optional | The quality of the image that will be generated.                   hd creates images with finer details and greater                   consistency across the image. This param is only supported for                   dall-e-3.| 
| response_format | string or null | Optional | The format in which the generated images are returned. Must be                   one of url or b64_json. URLs are                   only valid for 60 minutes after the image has been generated.| 
| size | string or null | Optional | The size of the generated images. Must be one of                   256x256, 512x512, or                   1024x1024 for dall-e-2. Must be one                   of 1024x1024, 1792x1024, or                   1024x1792 for dall-e-3 models.| 
| style | string or null | Optional | The style of the generated images. Must be one of                   vivid or natural. Vivid causes the                   model to lean towards generating hyper-real and dramatic                   images. Natural causes the model to produce more natural, less                   hyper-real looking images. This param is only supported for                   dall-e-3.| 
| user | string | Optional | A unique identifier representing your end-user, which can help                   OpenAI to monitor and detect abuse.                   Learn more.| 
## Returns 
Returns a list of
                [image](/docs/api-reference/images/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)
```

**Response**
```python
{
  "created": 1589478378,
  "data": [
    {
      "url": "https://..."
    },
    {
      "url": "https://..."
    }
  ]
}
```
