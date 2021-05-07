# Send custom header

```nginx
location /some {
  add_header X-custom-header some-value;
}
```

- add_header - will send custom header defined by name and value
- X-custom-header - name of custom header
- some-value - value of custom header
