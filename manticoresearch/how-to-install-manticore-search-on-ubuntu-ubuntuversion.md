# How to install Manticore search on Ubuntu UBUNTU_VERSION

```manticoresearch
wget http://repo.manticoresearch.com/manticore-repo.noarch.deb
dpkg -i manticore-repo.noarch.deb
apt update
apt install manticore manticore-columnar-lib
```

- `wget` - downloads official Manticoresearch deb
- `dpkg -i` - installs specified package from deb
- `apt update` - update installation repositories
- `apt install` - install selected packages
- `manticore` - Manticore search server
- `manticore-columnar-lib` - Additional storage for some types of indexes 


