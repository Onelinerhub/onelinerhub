# How to install PHP Symfony?
// plain

1. Download the Symfony installer using the command `curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony`
2. Make the installer executable using the command `chmod a+x /usr/local/bin/symfony`
3. Create a new Symfony project using the command `symfony new my_project_name`
4. Install the necessary dependencies using the command `composer install`
5. Start the built-in web server using the command `php bin/console server:run`

The output of the last command should be something like this:

```
[OK] Server listening on http://127.0.0.1:8000
```

You can now access your Symfony application in the browser at `http://127.0.0.1:8000`.

For more information, please refer to the [official Symfony documentation](https://symfony.com/doc/current/setup.html).

onelinerhub: [How to install PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-install-php-symfony)