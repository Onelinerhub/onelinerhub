# Send JSON data from file

```bash
curl https://httpbin.org/anything --data @data.json
```

- `curl` - base curl command
- `/anything` - sample URL to send request to
- `--data` - send specified data in the POST request
- `data.json` - name of the JSON file to load data from

group: json

## Example: 
```bash
curl https://httpbin.org/anything --data @data.json
```
```
{
  ...
  "form": {
    "{\"key\": \"value\"}": ""
  }, 
  ...
}
```

link_youtube: https://youtu.be/gls5n5iKuiM
