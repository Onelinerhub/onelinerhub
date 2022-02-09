# Set time series retention

```bash
redis-cli TS.ALTER ts_2 RETENTION 1000000
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ALTER` - change specified time series
- `ts_2` - name of time series
- `RETENTION` - sets retention in milliseconds from the time of last event in time series
- `1000000` - store values for a given time series only for `1000` seconds

group: create_delete

## Example: 
```bash
redis-cli TS.ALTER ts_2 RETENTION 1000000
```
```
OK
```

