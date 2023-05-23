# How to run a command in PHP Symfony?
// plain

To run a command in PHP Symfony, you can use the `bin/console` command. For example, to list all available commands, you can run the following command:

```
$ bin/console list
```

This will output a list of all available commands, such as:

```
help
list
assets:install
cache:clear
```

The `bin/console` command takes two arguments: the command name and the command options. The command name is the name of the command you want to run, and the command options are the arguments you want to pass to the command.

For example, to clear the cache, you can run the following command:

```
$ bin/console cache:clear
```

This will clear the cache and output a success message.

## Helpful links

- [Symfony Console](https://symfony.com/doc/current/console.html)
- [How to Use the Symfony Console](https://knpuniversity.com/screencast/symfony-console)

onelinerhub: [How to run a command in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-run-a-command-in-php-symfony)