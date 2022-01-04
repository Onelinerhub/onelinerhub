# Iterate through Redis keys

```python

```


## Example: 
```python
import redis

r = redis.Redis()
r.set('a', 1)


for k in r.scan_iter("*"):
  print(k, ': ', r.get(k))
```

