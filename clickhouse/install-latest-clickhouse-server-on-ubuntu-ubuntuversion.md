# Install latest Clickhouse server on Ubuntu UBUNTU_VERSION

```bash
apt install -y apt-transport-https ca-certificates dirmngr
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4
echo "deb https://repo.clickhouse.com/deb/stable/ main/" | sudo tee /etc/apt/sources.list.d/clickhouse.list
apt update && apt install -y clickhouse-server clickhouse-client
clickhouse start
```

- `apt install` - installs specified package on Ubuntu
- `apt-key adv` - sign Clickhouse official repo
- ` clickhouse-server` - Clickhouse server package
- `clickhouse-client` - CLI client
- `deb https://repo.clickhouse.com/deb/stable/ main/` - Add official Clickhouse repo to apt repositories list
- `clickhouse start` - start Clickhouse server


