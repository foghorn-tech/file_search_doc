# [Create image variation](/docs/api-reference/images/createVariation)
post https://api.openai.com/v1/images/variations 
Creates a variation of a given image. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| image | file | Required | The image to use as the basis for the variation(s). Must be a                   valid PNG file, less than 4MB, and square.| 
| model | string | Optional | The model to use for image generation. Only                   dall-e-2 is supported at this time.| 
| n | integer or null | Optional | The number of images to generate. Must be between 1 and 10.                   For dall-e-3, only n=1 is supported.| 
| response_format | string or null | Optional | The format in which the generated images are returned. Must be                   one of url or b64_json. URLs are                   only valid for 60 minutes after the image has been generated.| 
| size | string or null | Optional | The size of the generated images. Must be one of                   256x256, 512x512, or                   1024x1024.| 
| user | string | Optional | A unique identifier representing your end-user, which can help                   OpenAI to monitor and detect abuse.                   Learn more.| 
## Returns 
Returns a list of
                [image](/docs/api-reference/images/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
response = client.images.create_variation(
  image=open("image_edit_original.png", "rb"),
  n=2,
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
