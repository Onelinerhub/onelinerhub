# How do I configure Sphinx search to use an extension?
// plain

Configuring Sphinx search to use an extension is a simple process. First, you will need to install the extension via the command line. For example, if you wanted to install the [MySQLi extension](https://www.php.net/manual/en/mysqli.installation.php) you would use the following command:

```
$ sudo apt-get install php7.0-mysql
```

Once the extension is installed, you will need to enable it in the `php.ini` file. This can be done by adding the following line to the `php.ini` file:

```
extension=mysqli.so
```

After the extension is enabled, you will need to restart the web server for the changes to take effect. This can be done with the following command:

```
$ sudo service apache2 restart
```

Once the web server is restarted, you will be able to use the extension with Sphinx search.

## Code explanation

1. `$ sudo apt-get install php7.0-mysql` - Installs the extension via the command line
2. `extension=mysqli.so` - Enables the extension in the `php.ini` file
3. `$ sudo service apache2 restart` - Restarts the web server for the changes to take effect

## Helpful links
- [MySQLi Extension](https://www.php.net/manual/en/mysqli.installation.php)

onelinerhub: [How do I configure Sphinx search to use an extension?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinx-search-to-use-an-extension)