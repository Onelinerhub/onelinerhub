# Get info on time series

```bash
redis-cli TS.INFO ts_2
```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.INFO` - returns all system information on a given time series
- `ts_2` - name of time series

group: create_delete

## Example: 
```bash
redis-cli TS.INFO ts_2
```
```
 1) totalSamples
 2) (integer) 5
 3) memoryUsage
 4) (integer) 4293
 5) firstTimestamp
 6) (integer) 1644416919386
 7) lastTimestamp
 8) (integer) 1644417562711
 9) retentionTime
10) (integer) 1000000
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) (nil)
19) labels
20) 1) 1) "type"
       2) "test"
    2) 1) "group"
       2) "demo"
21) sourceKey
22) (nil)
23) rules
24) 1) 1) "ats_2"
       2) (integer) 60000
       3) SUM
```

