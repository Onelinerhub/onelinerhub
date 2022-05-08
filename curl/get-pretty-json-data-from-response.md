# Get pretty JSON data from response

```bash
curl -s https://examples.onelinerhub.com/json.json | jq .
```

- `curl` - base curl command
- `-s` - will not display any system information
- `/json.json` - sample JSON URL
- `|` - pipe downloaded response to the specified command
- `jq .` - will format specified JSON (downloaded from our URL)

group: json

## Example: 
```bash
curl -s https://examples.onelinerhub.com/json.json | jq .
```
```
{
  "key1": "value1",
  "key2": 2
}
```

link_youtube: https://youtu.be/7btK7bNQqgY
