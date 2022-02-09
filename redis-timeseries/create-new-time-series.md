# Create new time series

```redis
redis-cli TS.CREATE ts_2 LABELS test demo
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.CREATE` - creates specified time series
- `ts_2` - name of time series
- `LABELS` - list label for new time series
- `test demo` - add `test` and `demo` labels for our time series


