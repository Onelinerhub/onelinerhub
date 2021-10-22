# Get all keys of some command's json output

```bash
somecommand | jq 'keys | .[]'
```

- somecommand - any command that has to output json, `echo '{ "a": 1, "b": 2 }'` for example
- 'keys | .[]' - keys of the object (not the values) as an array
