# OpenAI API example in Python
// plain

OpenAI API is a Python library that allows developers to access OpenAI's services and use them in their applications.

## Example code

```
import openai
openai.api_key = "YOUR_API_KEY"
response = openai.Completion.create(
    engine="davinci",
    prompt="The quick brown fox",
    max_tokens=50
)
```

onelinerhub: [OpenAI API example in Python
](https://onelinerhub.com/python-openai/openai-api-example-in-python)
