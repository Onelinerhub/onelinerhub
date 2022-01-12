# Install latest Clickhouse server on Ubuntu UBUNTU_VERSION

```sql
apt install -y apt-transport-https ca-certificates dirmngr
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4
apt update && apt install -y clickhouse-server clickhouse-client
```

- `apt install` - installs specified package on Ubuntu
- `apt-key adv` - sign Clickhouse official repo
- ` clickhouse-server` - Clickhouse server package
- `clickhouse-client` - CLI client


