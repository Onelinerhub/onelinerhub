# How to generate password in CLI

```bash
openssl rand -base64 12
```

- `openssl` - utility to manage SSL functionality
- `rand` - generate random key
- `-base64` - convert key to base64
- `12` - approximate length of generated password 

group: pwd

## Example: 
```bash
openssl rand -base64 12
```
```
8U2ZA+VndUyxTiYn
```

