# Delete time series key

```bash
redis-cli DEL ts_1

```

- `redis-cli` - redis executable with [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) module installed
- `DEL` - standard `DEL` command will remove time series keys also
- `ts_1` - name of time series to remove

group: create_delete

## Example: 
```bash
redis-cli DEL ts_1
```
```
(integer) 1
```

