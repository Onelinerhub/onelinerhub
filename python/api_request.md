# Make API Request
```python
import requests

url = "http://www.boredapi.com/api/activity/"
response = (requests.get(url).json())
print(response)
```

- requests - library to make HTTP requests
- url - API endpoint 
- request.get() - function returns a response 
- json() - fucntion converts to JSON object
- print - displaying the response
