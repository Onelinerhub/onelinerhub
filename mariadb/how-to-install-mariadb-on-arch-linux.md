# How to install Mariadb on Arch linux?
// plain

1. Install Mariadb on Arch Linux using the `pacman` package manager:
```
sudo pacman -S mariadb
```
2. After installation, initialize the database:
```
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```
3. Start the MariaDB service:
```
sudo systemctl start mariadb
```
4. Secure the installation by running the `mysql_secure_installation` script:
```
sudo mysql_secure_installation
```
5. To enable MariaDB to start on boot, run:
```
sudo systemctl enable mariadb
```

Detailed explanation:

1. `sudo pacman -S mariadb`: This command installs the MariaDB package from the Arch Linux repository.

2. `sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`: This command initializes the MariaDB database.

3. `sudo systemctl start mariadb`: This command starts the MariaDB service.

4. `sudo mysql_secure_installation`: This command runs the `mysql_secure_installation` script, which sets up a root password and removes anonymous users and test databases.

5. `sudo systemctl enable mariadb`: This command enables MariaDB to start on boot.

## Helpful links

- [Arch Linux Wiki - MariaDB](https://wiki.archlinux.org/index.php/MariaDB)
- [Arch Linux Wiki - MySQL](https://wiki.archlinux.org/index.php/MySQL)

onelinerhub: [How to install Mariadb on Arch linux?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-arch-linux)