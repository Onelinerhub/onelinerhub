# Get time series latest value

```bash
redis-cli TS.GET ts_2
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.GET` - returns last value for a given time series
- `ts_2` - name of time series

group: get_data

## Example: 
```bash
redis-cli TS.GET ts_2
```
```
1) (integer) 1644417562711
2) 14
```

