# Python Redis time series example

### This examples is based on [Redis Timeseries](https://onelinerhub.com/redis-timeseries) module:

```python
r = redis.Redis()
list = r.eval("return redis.call('TS.RANGE', 'ts_2', 1644415000020, 1644417094099)", 0)

```

- `redis.Redis` - connect to Redis server
- `eval` - executes Lua script
- `redis.call` - calls RAW Redis command
- `TS.RANGE` - [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) command to get time series range
- `ts_2` - name of the time series object
- `1644415000020` - start timestamp (in microseconds)
- `1644417094099` - end timestamp (in microseconds)

## Example: 
```python
import redis

r = redis.Redis()
list = r.eval("return redis.call('TS.RANGE', 'ts_2', 1644415000020, 1644417094099)", 0)
print(list)
```
```
[[1644416919386, b'12'], [1644416925338, b'14'], [1644417094095, b'15']]

```

