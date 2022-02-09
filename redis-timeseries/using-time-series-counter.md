# Using time series counter

```bash
redis-cli TS.INCRBY tsc 1
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.INCRBY` - increment given time series last value by a specified number
- `tsc` - name of time series (will be created automatically if absent)
- `1` - step to increment by

## Example: 
```bash
TS.INCRBY tsc 1
TS.INCRBY tsc 1
TS.INCRBY tsc 1
redis-cli TS.GET tsc
```
```
1) (integer) 1644418537849
2) 3
```

