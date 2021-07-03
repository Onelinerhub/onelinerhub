# Track time taken by request

```bash
curl -w %{time_total} https://example.org/
```

- -w - writes specified variables after request is completed
- %{time_total} - will print total time of the request right after request output ([see formats you can use](https://everything.curl.dev/usingcurl/verbose/writeout))
- example.org - example request URL
