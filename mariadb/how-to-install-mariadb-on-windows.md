# How to install Mariadb on Windows?
// plain

1. Download the Mariadb installer from the [official website](https://downloads.mariadb.org/).
2. Run the installer and follow the instructions.
3. Select the components you want to install.
4. Set the root password for the database.
5. Click the "Execute" button to start the installation.

You can also install Mariadb from the command line using the following command:

```
msiexec /i mariadb-10.4.13-winx64.msi /qn
```

This command will install Mariadb with the default settings.

You can also specify additional parameters to customize the installation. For example, to set the root password for the database, you can use the following command:

```
msiexec /i mariadb-10.4.13-winx64.msi /qn ROOT_PASSWORD=<password>
```

The command above will install Mariadb and set the root password to the specified value.

You can find more information about the available parameters in the [Mariadb documentation](https://mariadb.com/kb/en/library/installing-mariadb-msi-packages-on-windows/).

onelinerhub: [How to install Mariadb on Windows?](https://onelinerhub.com/mariadb/how-to-install-mariadb-on-windows)