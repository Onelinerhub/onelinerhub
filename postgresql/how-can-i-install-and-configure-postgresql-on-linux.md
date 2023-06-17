# How can I install and configure PostgreSQL on Linux?
// plain

1. Download and install PostgreSQL from the official website: [https://www.postgresql.org/download/linux/](https://www.postgresql.org/download/linux/).
2. Create a `postgres` user and a `postgres` group:
```
sudo useradd -r -m -d /var/lib/postgresql -s /bin/bash -c "PostgreSQL Server" -U postgres
```
3. Create a `/var/lib/postgresql` directory and set the correct permissions for the `postgres` user and group:
```
sudo mkdir /var/lib/postgresql
sudo chown postgres:postgres /var/lib/postgresql
```
4. Initialize the database cluster:
```
sudo -u postgres initdb -D /var/lib/postgresql/data
```
5. Configure PostgreSQL to start on boot:
```
sudo systemctl enable postgresql
```
6. Start the PostgreSQL service:
```
sudo systemctl start postgresql
```
7. Connect to the PostgreSQL server and create a database:
```
sudo -u postgres psql
CREATE DATABASE my_database;
```

* `useradd` is used to create a user and a group.
* `mkdir` is used to create a directory.
* `chown` is used to set the correct permissions for the user and group.
* `initdb` is used to initialize the database cluster.
* `systemctl enable` is used to configure PostgreSQL to start on boot.
* `systemctl start` is used to start the PostgreSQL service.
* `psql` is used to connect to the PostgreSQL server.
* `CREATE DATABASE` is used to create a database.

onelinerhub: [How can I install and configure PostgreSQL on Linux?](https://onelinerhub.com/postgresql/how-can-i-install-and-configure-postgresql-on-linux)