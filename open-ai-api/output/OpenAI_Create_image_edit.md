# [Create image edit](/docs/api-reference/images/createEdit)
post https://api.openai.com/v1/images/edits 
Creates an edited or extended image given an original image and a
          prompt. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| image | file | Required | The image to edit. Must be a valid PNG file, less than 4MB,                   and square. If mask is not provided, image must have                   transparency, which will be used as the mask.| 
| prompt | string | Required | A text description of the desired image(s). The maximum length                   is 1000 characters.| 
| mask | file | Optional | An additional image whose fully transparent areas (e.g. where                   alpha is zero) indicate where image should be                   edited. Must be a valid PNG file, less than 4MB, and have the                   same dimensions as image.| 
| model | string | Optional | The model to use for image generation. Only                   dall-e-2 is supported at this time.| 
| n | integer or null | Optional | The number of images to generate. Must be between 1 and 10.| 
| size | string or null | Optional | The size of the generated images. Must be one of                   256x256, 512x512, or                   1024x1024.| 
| response_format | string or null | Optional | The format in which the generated images are returned. Must be                   one of url or b64_json. URLs are                   only valid for 60 minutes after the image has been generated.| 
| user | string | Optional | A unique identifier representing your end-user, which can help                   OpenAI to monitor and detect abuse.                   Learn more.| 
## Returns 
Returns a list of
                [image](/docs/api-reference/images/object) objects. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
client.images.edit(
  image=open("otter.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A cute baby sea otter wearing a beret",
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
