# How to add new proxy to proxychains

### Edit config file (usually located at `/etc/proxychains.conf`):

```txt
#...
[ProxyList]
socks4 1.2.3.4 1234
socks4 1.2.3.5 1235

```

- `[ProxyList]` - list of proxies to use
- `socks4 1.2.3.4 1234` - first proxy
- `socks4 1.2.3.5 1235` - second proxy (add as many as you need)


