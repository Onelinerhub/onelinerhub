# Increase upstream buffers ("Upstream sent too big header" error)

```nginx
proxy_buffer_size   64k;
proxy_buffers       16 64k;
fastcgi_buffer_size 64k;
fastcgi_buffers     16 64k;
```

- proxy_buffer_size   64k - will increase proxy buffer size to 64k (from default 8k)
- proxy_buffers       16 - we will have 16 buffers available (from default 8)
- fastcgi_buffers - the same as ```proxy_buffers``` but for PHP
- astcgi_buffer_size - the same as ```proxy_buffer_size``` but for PHP
