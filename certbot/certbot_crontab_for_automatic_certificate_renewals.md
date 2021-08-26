# Certbot crontab for automatic certificate renewals

```bash
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

0 */12 * * * root test -x /usr/bin/certbot -a \! -d /run/systemd/system && perl -e 'sleep int(rand(43200))' && certbot -q renew
```

- 0 */12 - will launch renewal checker every 12 hours
- certbot -q renew - command to renew certificates
