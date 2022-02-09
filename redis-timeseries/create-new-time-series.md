# Create new time series

```bash
redis-cli TS.CREATE ts_2 LABELS type demo

```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `TS.CREATE` - creates specified time series
- `ts_2` - name of time series
- `LABELS` - list label for new time series
- `type demo` - add `type` label with `demo` value

## Example: 
```bash
redis-cli TS.CREATE ts_3 LABELS test demo

redis-cli TS.INFO ts_3
```
```
OK

 1) totalSamples
 2) (integer) 0
 3) memoryUsage
 4) (integer) 4210
 5) firstTimestamp
 6) (integer) 0
 7) lastTimestamp
 8) (integer) 0
 9) retentionTime
10) (integer) 0
11) chunkCount
12) (integer) 1
13) chunkSize
14) (integer) 4096
15) chunkType
16) compressed
17) duplicatePolicy
18) (nil)
19) labels
20) 1) 1) "test"
       2) "demo"
21) sourceKey
22) (nil)
23) rules
24) (empty list or set)
```

