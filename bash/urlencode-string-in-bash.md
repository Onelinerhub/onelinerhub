# Urlencode string in bash

```bash
printf %s 'some string' | jq -sRr @uri
```

- `printf %s` - will print specified string with no quotes
- `jq` - a tool to work with JSON, but we'll use it for encoding here
- `-sRr @uri` - will encode given value using urlencoding

## Example: 
```bash
printf %s 'some string' | jq -sRr @uri
```
```
some%20string
```

