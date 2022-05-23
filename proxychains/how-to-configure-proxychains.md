# How to configure proxychains

### Edit `/etc/proxychains.conf` file to configure `proxychains`:

```txt
[ProxyList]
socks5	1.2.3.4	123	user	pwd
```

- `[ProxyList]` - configuration block to list available proxies
- `socks5` - proxy type
- `1.2.3.4` - proxy address
- `123` - proxy port
- `user` - proxy authentication username
- `pwd` - proxy authentication password

group: install


