# [Create moderation](/docs/api-reference/moderations/create)
post https://api.openai.com/v1/moderations 
Classifies if text is potentially harmful. 
## Request body 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| input | string or array | Required | The input text to classify| 
| model | string | Optional | Two content moderations models are available:                   text-moderation-stable and                   text-moderation-latest.                                     The default is text-moderation-latest which will                   be automatically upgraded over time. This ensures you are                   always using our most accurate model. If you use                   text-moderation-stable, we will provide advanced                   notice before updating the model. Accuracy of                   text-moderation-stable may be slightly lower than                   for text-moderation-latest.| 
## Returns 
A
                [moderation](/docs/api-reference/moderations/object)
                object. 

**Example request**
```python
from openai import OpenAI
client = OpenAI()
moderation = client.moderations.create(input="I want to kill them.")
print(moderation)
```

**Response**
```python
{
  "id": "modr-XXXXX",
  "model": "text-moderation-005",
  "results": [
    {
      "flagged": true,
      "categories": {
        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": true,
        "violence": true,
      },
      "category_scores": {
        "sexual": 1.2282071e-06,
        "hate": 0.010696256,
        "harassment": 0.29842457,
        "self-harm": 1.5236925e-08,
        "sexual/minors": 5.7246268e-08,
        "hate/threatening": 0.0060676364,
        "violence/graphic": 4.435014e-06,
        "self-harm/intent": 8.098441e-10,
        "self-harm/instructions": 2.8498655e-11,
        "harassment/threatening": 0.63055265,
        "violence": 0.99011886,
      }
    }
  ]
}
```
