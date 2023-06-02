# How do I set up Valet to use PHP and Redis?
// plain

1. First, you need to install Valet and its dependencies. This can be done using [Composer](https://getcomposer.org/):

```
composer global require laravel/valet
```

2. Once Valet is installed, you need to configure it to use PHP and Redis. This can be done by editing the `~/.valet/config.json` file.

3. Add the following lines to the `config.json` file to enable PHP and Redis:

```
"env": {
    "php": "/usr/bin/php",
    "redis": "/usr/bin/redis-server"
}
```

4. Once the configuration is saved, you need to restart Valet to apply the changes. This can be done using the following command:

```
valet restart
```

5. Finally, you can verify that PHP and Redis are enabled by running `valet env` in the terminal:

```
$ valet env
PHP: /usr/bin/php
Redis: /usr/bin/redis-server
```

That's it! You have successfully set up Valet to use PHP and Redis.

onelinerhub: [How do I set up Valet to use PHP and Redis?](https://onelinerhub.com/predis/how-do-i-set-up-valet-to-use-php-and-redis)