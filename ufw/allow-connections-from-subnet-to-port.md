# Allow connections from subnet to port

```ufw
ufw allow from 1.2.3.0/24 proto tcp to any port 80
```

- `from 1.2.3.0/24` - specify subnet to allow connections from
- `proto tcp` - tcp protocol only
- `to any port 80` - allow connections to HTTP port

group: subnet


## Additional keywords
- network
- open
- accept
