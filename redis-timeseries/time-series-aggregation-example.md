# Time series aggregation example

### You can create special aggregation rules for time series keys to compress them based on bigger ranges (to save data):

```bash
redis-cli TS.CREATE ats_2
redis-cli TS.CREATERULE ts_2 ats_2 AGGREGATION sum 60000
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.CREATE ats_2` - create `ats_2` time series that will be used for aggregated data from `ts_2`
- `TS.CREATERULE` - crates aggregation rule
- `ts_2 ats_2` - save aggregated data from `ts_2` key to `ats_2` key
- `AGGREGATION` - specify aggregation options
- `sum` - aggregation function to use ([list of supported functions](https://oss.redis.com/redistimeseries/commands/#tscreaterule))
- `60000` - timebucket to aggregate on in milliseconds (`60` seconds in our case)


