# Get time series data by interval

```bash
redis-cli TS.RANGE ts_2 1644415000020 1644417094099
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.RANGE` - return time series values for a given time range
- `ts_2` - name of time series
- `1644415000020` - timestamp to start from
- `1644417094099` - timestamp to end range

## Example: 
```bash
redis-cli TS.RANGE ts_2 1644415000020 1644417094099
```
```
1) 1) (integer) 1644416919386
   2) 12
2) 1) (integer) 1644416925338
   2) 14
3) 1) (integer) 1644417094095
   2) 15
```

