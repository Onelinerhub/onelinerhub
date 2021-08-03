# How to install php swoole.

```bash
apt install php-dev php-pear
pecl install swoole
bash -c "echo 'extension=swoole' >> $(php -i | grep /.+/php.ini -oE)"
```

- php-dev - php development tools
- pecl - native php package manager
- swoole - lib we want to install (will take a while)
- echo 'extension=swoole' - add swoole extension loader to php.ini config file (cli version)
