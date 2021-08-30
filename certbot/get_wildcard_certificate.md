# Get wildcard certificate

```bash
certbot certonly -d *.example.com
```

- certonly - issue certificate without any further steps
- -d - specify domain (wildcard in our case) to issue certificate for
