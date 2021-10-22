# Filter property in some command's json output 

```bash
somecommand | jq '.foo'
```

- somecommand - any command that has to output json, `echo '{ "foo": 123, "bar": 456 }'` for example
- '.foo' - json property name in output of a command
