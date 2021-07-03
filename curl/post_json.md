# How to post JSON data

```bash
curl -H "Content-Type: application/json" -X POST -d '{"var1":"val1"}' https://example.org/script.php
```

- Content-Type: application/json - set JSON content type for our request
- -X POST - make this a POST request
- -d - specify data we want to post
- '{"var1":"val1"}' - JSON in plain text we're going to post
- example.org/script.php - example script to post data to

group: post
