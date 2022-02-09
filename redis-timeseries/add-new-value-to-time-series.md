# Add new value to time series

```bash
redis-cli TS.ADD ts_2 \* 15
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ADD` - adds new time/value pair to given time series
- `ts_2` - name of time series
- `\*` - will set current time (or specify timestamp in milliseconds) for a given value
- `15` - value to store for a given time


