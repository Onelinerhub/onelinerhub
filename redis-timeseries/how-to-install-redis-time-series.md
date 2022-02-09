# How to install Redis time series

### Before installing [download RedisTimeSeries module](https://redis.com/redis-enterprise-software/download-center/modules/) and unpack into `/var/lib/redis` (or other) folder. Then edit `/etc/redis/redis.conf`:

```txt
loadmodule /var/lib/redis/redistimeseries.so

```

- `loadmodule` - configuration parameter that loads additional module
- `/var/lib/redis/redistimeseries.so` - path to downloaded and unpacked module file


