# [Training format for completions models](/docs/api-reference/fine-tuning/completions-input)
The per-line training example of a fine-tuning input file for
          completions models 
| Parameter | Type   | Required | Description|
| --- | --- | --- | --- |
| prompt | string | Optional | The input prompt for this training example.| 
| completion | string | Optional | The desired completion for this training example.| 

**Training format for completions models**
```python
{
  "prompt": "What is the answer to 2+2",
  "completion": "4"
}
```
