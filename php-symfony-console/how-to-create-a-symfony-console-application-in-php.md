# How to create a Symfony console application in PHP?
// plain

Creating a Symfony console application in PHP is a simple process.

First, create a new project using the Symfony CLI:
```
$ symfony new my_project
```

This will create a new project in the `my_project` directory.

Next, create a new command class in the `src/Command` directory:
```
$ touch src/Command/MyCommand.php
```

The command class should extend the `Symfony\Component\Console\Command\Command` class and implement the `configure()` and `execute()` methods.

Finally, register the command in the `config/services.yaml` file:
```
services:
    App\Command\MyCommand:
        tags:
            - { name: console.command }
```

The command can now be executed using the Symfony CLI:
```
$ php bin/console my:command
```

## Helpful links
- [Symfony Console Component](https://symfony.com/doc/current/components/console.html)
- [Creating a Command](https://symfony.com/doc/current/console.html#creating-a-command)

onelinerhub: [How to create a Symfony console application in PHP?](https://onelinerhub.com/php-symfony-console/how-to-create-a-symfony-console-application-in-php)