# Install NJS (Nginx Javascript) module

```bash
apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list
apt update
apt install nginx-module-njs
```

- `apt install` - installs specified package on Ubuntu
- `nginx-module-njs` - Nginx NJs module

group: njs


