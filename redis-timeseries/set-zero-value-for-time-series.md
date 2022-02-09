# Set zero value for time series

```bash
redis-cli TS.ADD ts_2 \* 0
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `ts_2` - name of time series
- `TS.ADD` - adds new time/value pair to given time series
- `\*` - will set current time (or specify timestamp in milliseconds) for a given value

## Example: 
```bash
redis-cli TS.ADD ts_2 \* 0
```
```
OK
```

