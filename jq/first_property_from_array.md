# Get first item property in some command's json output

```bash
somecommand | jq '.[0]'
```

- somecommand - any command that has to output json, `echo '["foo", "bar"]'` for example
- '.[0-∞]' - address/point of item in array of items (0 -> first, 1 -> second, etc.)
