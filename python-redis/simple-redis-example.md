# Simple Redis example

```python
import redis

r = redis.Redis()

r.set('k', 'hi')

print(r.get('k').decode('utf-8'))
```



