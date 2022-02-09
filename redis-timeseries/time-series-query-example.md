# Time series query example

```bash
redis-cli TS.RANGE ts_2 1644415000020 1644417094099 COUNT 2 AGGREGATION sum 3600000
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.RANGE` - return time series values for a given time range
- `ts_2` - name of time series
- `1644415000020 1644417094099` - timestamp range in milliseconds to select values within 
- `COUNT` - limits resulting values
- `2` - return not more than 2 values
- `AGGREGATION` - aggregate result based on options
- `sum` - aggregating function to use ([list of supported functions](https://oss.redis.com/redistimeseries/commands/#tscreaterule))
- `3600000` - time bucket in milliseconds to aggregate on (1 hour in our case)


