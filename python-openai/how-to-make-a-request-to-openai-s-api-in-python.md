# How to make a request to OpenAI's API in Python?
// plain

Making a request to OpenAI's API in Python is easy and straightforward. The following example code block shows how to make a request to the API using the `requests` library:

```python
import requests

url = 'https://api.openai.com/v1/engines/davinci/completions'

data = {
  "prompt": "The quick brown fox",
  "max_tokens": 50
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer <YOUR_API_KEY>"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
```

The output of the example code is:

```
{
  "id": "davinci_<SOME_ID>",
  "object": "text_completion",
  "choices": [
    {
      "text": "The quick brown fox jumped over the lazy dog.",
      "index": 0,
      "logprobs": [
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945,
        -4.945
      ]
    }
  ]
}
```

## Code explanation


1. `import requests`: This imports the `requests` library which is used to make the API request.
2. `url = 'https://api.openai.com/v1/engines/davinci/completions'`: This sets the URL of the API endpoint.
3. `data = { "prompt": "The quick brown fox", "max_tokens": 50 }`: This sets the data to be sent in the request body.
4. `headers = { "Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>" }`: This sets the headers of the request.
5. `response = requests.post(url, json=data, headers=headers)`: This makes the API request using the `requests.post()` method.
6. `print(response.json())`: This prints the response from the API.

For more information, please refer to the [OpenAI API documentation](https://openai.com/docs/api-reference/).
Also check [Quick start guide for OpenAI API and Python](https://datachild.net/machinelearning/openai-api-python-quickstart).

onelinerhub: [How to make a request to OpenAI's API in Python?](https://onelinerhub.com/python-openai/how-to-make-a-request-to-openai-s-api-in-python)
