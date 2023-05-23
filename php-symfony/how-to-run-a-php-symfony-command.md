# How to run a PHP Symfony command?
// plain

To run a PHP Symfony command, you can use the `bin/console` command. For example, to list all available commands, you can run the following command:

```
$ bin/console
```

This will output a list of all available commands:

```
  about
  assets
  cache
  debug
  ...
```

The `bin/console` command takes two arguments: the command name and the command options. For example, to clear the cache, you can run the following command:

```
$ bin/console cache:clear
```

This will clear the cache and output the following message:

```
Cache for the "dev" environment (debug=true) was successfully cleared.
```

The `bin/console` command is the main entry point for running Symfony commands. For more information, please refer to the [Symfony Console Component](https://symfony.com/doc/current/components/console.html) documentation.

onelinerhub: [How to run a PHP Symfony command?](https://onelinerhub.com/php-symfony/how-to-run-a-php-symfony-command)