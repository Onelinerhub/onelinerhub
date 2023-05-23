# How to install PHP PCNTL extension in Docker?
// plain

To install the PHP PCNTL extension in Docker, you need to add the following line to your `Dockerfile`:

```
RUN docker-php-ext-install pcntl
```

This will install the PCNTL extension in your Docker container.

You can then verify that the extension is installed by running the following command:

```
php -m | grep pcntl
```

The output should be:

```
pcntl
```

For more information, please refer to the [PHP PCNTL documentation](https://www.php.net/manual/en/book.pcntl.php).

onelinerhub: [How to install PHP PCNTL extension in Docker?](https://onelinerhub.com/php-pcntl/how-to-install-php-pcntl-extension-in-docker)