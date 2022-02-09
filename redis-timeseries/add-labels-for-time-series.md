# Add labels for time series

```bash
redis-cli TS.ALTER ts_2 LABELS type test group demo
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ALTER` - change specified time series
- `ts_2` - name of time series
- `LABELS` - list label for specified time series
- `type test group demo` - add `type` label with `test` value and `group` label with `demo` value

## Example: 
```bash
redis-cli TS.ALTER ts_2 LABELS test demo tmp
```
```
OK
```

