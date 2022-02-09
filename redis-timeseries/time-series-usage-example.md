# Time series usage example

```bash
redis-cli TS.ADD ts1 \* 1
redis-cli TS.ADD ts1 \* 3
redis-cli TS.ADD ts1 \* 8
redis-cli TS.RANGE ts1 1644418370178 1644418371267
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.ADD` - adds new time/value pair to given time series
- `ts1` - name of time series we'll use
- `\*` - use current time as a timestamp when we add new value to our time series
- `TS.RANGE` - return time series values for a given time range
- `1644418370178 1644418371267` - timestamp range (in milliseconds) to get values within

## Example: 
```bash
redis-cli TS.ADD ts \* 1
redis-cli TS.ADD ts \* 3
redis-cli TS.ADD ts \* 8

redis-cli TS.RANGE ts 1644418370178 1644418371267
```
```
(integer) 1644418370178
(integer) 1644418370181
(integer) 1644418371267

1) 1) (integer) 1644418370178
   2) 1
2) 1) (integer) 1644418370181
   2) 3
3) 1) (integer) 1644418371267
   2) 8

```

