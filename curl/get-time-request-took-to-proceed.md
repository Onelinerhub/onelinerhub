# Get time request took to proceed

```bash
curl -o /dev/null -s -w "%{time_total}s\n" https://onelinerhub.com
```

- `curl` - base curl command
- `-o /dev/null` - will ask curl to skip response body
- `-w` - will ask curl to display specified data about request
- `%{time_total}` - will show total time it took request to process (in seconds)
- `https://onelinerhub.com` - sample URL to request

## Example: 
```bash
curl -o /dev/null -s -w "%{time_total}s\n" https://onelinerhub.com
```
```
0.146088s
```

link_youtube: https://youtu.be/XFmI3ZnU2ik
