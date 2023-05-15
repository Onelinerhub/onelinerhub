# How to install Mariadb on Centos?
// plain

1. Install Mariadb on Centos by running the following command:
```
sudo yum install mariadb-server mariadb
```
2. Start the Mariadb service by running the following command:
```
sudo systemctl start mariadb
```
3. Secure the Mariadb installation by running the following command:
```
sudo mysql_secure_installation
```
4. Test the Mariadb installation by running the following command:
```
mysql -u root -p
```
5. For more information, please refer to the [Mariadb Documentation](https://mariadb.com/kb/en/library/installing-mariadb-on-centos/).

onelinerhub: [How to install Mariadb on Centos?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-centos)