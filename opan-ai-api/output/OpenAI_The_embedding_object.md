# [The embedding object](/docs/api-reference/embeddings/object)
Represents an embedding vector returned by embedding endpoint. 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| index | integer | Optional | The index of the embedding in the list of embeddings.| 
| embedding | array | Optional | The embedding vector, which is a list of floats. The length of                 vector depends on the model as listed in the                 embedding guide.| 
| object | string | Optional | The object type, which is always "embedding".| 

**The embedding object**
```python
{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
```
