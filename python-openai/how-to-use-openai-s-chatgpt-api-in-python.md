# How to use OpenAI's ChatGPT API in Python?
// plain

OpenAI's ChatGPT API is a natural language processing (NLP) model that can be used to generate human-like conversations. It can be used in Python with the OpenAI SDK.

## Example code

```
import openai
openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
    engine="davinci",
    prompt="Hello, how are you?",
    temperature=0.7,
    max_tokens=50,
)

print(response.choices[0].text)
```

## Output example

```
I'm doing great, thank you!
```

## Code explanation


1. `import openai`: imports the OpenAI SDK.
2. `openai.api_key = "YOUR_API_KEY"`: sets the API key for authentication.
3. `response = openai.Completion.create(...)`: creates a completion object with the given parameters.
4. `temperature=0.7`: sets the temperature of the response, which controls the randomness of the response.
5. `max_tokens=50`: sets the maximum number of tokens in the response.
6. `print(response.choices[0].text)`: prints the text of the first choice in the response.

## Helpful links

- [OpenAI SDK Documentation](https://openai.com/docs/sdk/)
- [ChatGPT Documentation](https://openai.com/blog/chatgpt/)

onelinerhub: [How to use OpenAI's ChatGPT API in Python?](https://onelinerhub.com/python-openai/how-to-use-openai-s-chatgpt-api-in-python)