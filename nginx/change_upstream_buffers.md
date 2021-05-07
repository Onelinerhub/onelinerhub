# Increase upstream buffers ("Upstream sent too big header" error)

```nginx
proxy_buffer_size 64k;
proxy_buffers     16 64k;
```

- 64k - will increase proxy buffer size to 64k (from default 8k)
-  16 - we will have 16 buffers available (from default 8)
