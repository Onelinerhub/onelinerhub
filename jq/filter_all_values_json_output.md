# Get all values of some command's json output 

```bash
somecommand | jq '.[]'
```

- somecommand - any command that has to output json, `echo '{ "a": 1, "b": 2 }'` for example
- '.[]' - provide the value of each key/value pair
