# How to create certificate for multiple domains

```bash
certbot certonly -d example.com,mob.example.com,www.example.com
```

- certonly - just issues certificate without further steps
- -d - specify list of domain to issue certificate for
