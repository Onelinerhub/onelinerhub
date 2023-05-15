# How to install Mariadb on Debian?
// plain

1. Install Mariadb on Debian using the following command:
```
sudo apt-get install mariadb-server
```
2. After the installation is complete, run the following command to secure the installation:
```
sudo mysql_secure_installation
```
3. You will be prompted to enter a password for the root user. Enter a secure password and press enter.
4. You will be asked a series of questions. Answer them according to your preferences.
5. Finally, run the following command to start the Mariadb service:
```
sudo systemctl start mariadb
```

## Helpful links
- [How to Install MariaDB on Debian 10](https://linuxize.com/post/how-to-install-mariadb-on-debian-10/)
- [MariaDB Documentation](https://mariadb.com/kb/en/library/getting-installing-and-upgrading-mariadb/)

onelinerhub: [How to install Mariadb on Debian?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-debian)