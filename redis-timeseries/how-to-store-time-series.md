# How to store time series

### You can store time series by setting values for time series key, [created](https://onelinerhub.com/redis-timeseries/create-new-time-series) earlier (or it will be created automatically):

```bash
redis-cli TS.ADD ts_2 1644415010024 12
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ADD` - adds new time/value pair to given time series
- `ts_2` - name of time series
- `1644415010024` - timestamp of a value to insert
- `12` - value to insert for a given timestamp

## Example: 
```bash
redis-cli TS.ADD ts_2 1644416919386 12
TS.RANGE ts_2 1644416919385 1644416919387
```
```
1) 1) (integer) 1644416919386
   2) 12
```

