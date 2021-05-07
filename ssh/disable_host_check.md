# Disable host key check ("The Authenticity Of Host Can’t Be Established" error)

```bash
ssh -o StrictHostKeyChecking=no user@server.com
```

- -o StrictHostKeyChecking=no - disables strict host key checks
- user@server.com - remote user and server address
