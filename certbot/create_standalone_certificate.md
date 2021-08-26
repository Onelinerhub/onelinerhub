# Create standalone certificate

Make sure to stop your webserver when running this command.

```bash
certbot certonly --standalone -d example.org -m my@mail.com --agree-tos
```

- certonly - asks certbot to create certificate only in `/etc/letsencrypt/live`
- --standalone - launches built-in webserver to verify domain ownership
- -d example.org - domain we want to create certificate for
- -m my@mail.com - email to use as a main contact
- --agree-tos - automatically confirm terms aggrement
