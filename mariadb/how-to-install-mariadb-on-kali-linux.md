# How to install Mariadb on Kali linux?
// plain

1. Install Mariadb on Kali Linux by running the following command in the terminal:
```
sudo apt-get install mariadb-server
```
2. After the installation is complete, you will be prompted to set a root password for the database.
3. Once the root password is set, you can start the MariaDB service by running the following command:
```
sudo systemctl start mariadb
```
4. To check if the service is running, use the following command:
```
sudo systemctl status mariadb
```
5. You should see an output similar to this:
```
● mariadb.service - MariaDB 10.3.22 database server
   Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2020-09-14 11:45:45 UTC; 1min 10s ago
 Main PID: 809 (mysqld)
    Tasks: 27 (limit: 4704)
   Memory: 4.3M
   CGroup: /system.slice/mariadb.service
           └─809 /usr/sbin/mysqld
```

## Helpful links
- [Kali Linux Documentation - Installing MariaDB](https://docs.kali.org/general-use/install-mariadb-on-kali-linux)

onelinerhub: [How to install Mariadb on Kali linux?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-kali-linux)