# How to install Mariadb on Ubuntu?
// plain

1. Install Mariadb on Ubuntu using the following command:
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
- [How To Install MariaDB on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-18-04)
- [How To Secure MariaDB on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-secure-mariadb-on-ubuntu-18-04)

onelinerhub: [How to install Mariadb on Ubuntu?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-ubuntu)