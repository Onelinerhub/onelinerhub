# Add labels for time series

```bash
redis-cli TS.ALTER ts_2 LABELS test demo tmp
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ALTER` - change specified time series
- `ts_2` - name of time series
- `LABELS` - list label for specified time series
- `test demo tmp` - list of labels to assign to time series

## Example: 
```bash
redis-cli TS.ALTER ts_2 LABELS test demo tmp
```
```
OK
```

