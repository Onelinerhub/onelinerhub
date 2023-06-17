# How can I set up and configure a PostgreSQL server?
// plain

1. Install PostgreSQL using a package manager:
```
sudo apt-get install postgresql
```

2. Create a database user:
```
sudo -u postgres createuser -s <username>
```

3. Create a new database:
```
sudo -u postgres createdb <dbname>
```

4. Configure authentication for the user:
```
sudo -u postgres psql
\password <username>
```

5. Allow remote connections (optional):
Edit the file `/etc/postgresql/<version>/main/pg_hba.conf` and add the line:
```
host <dbname> <username> <IP address> md5
```

6. Edit the PostgreSQL configuration file `postgresql.conf` to allow remote connections:
Change the line `listen_addresses = 'localhost'` to `listen_addresses = '*'`

7. Restart the PostgreSQL service:
```
sudo service postgresql restart
```

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [How To Install and Use PostgreSQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

onelinerhub: [How can I set up and configure a PostgreSQL server?](https://onelinerhub.com/postgresql/how-can-i-set-up-and-configure-a-postgresql-server)