# How to deploy a Symfony application?
// plain

Deploying a Symfony application is a straightforward process.

1. Install the Symfony CLI tool:
```
$ curl -sS https://get.symfony.com/cli/installer | bash
```
2. Create a Symfony project:
```
$ symfony new my_project
```
3. Configure the web server:
- Create a virtual host for the project
- Set the document root to the `public` directory of the project
- Configure the web server to use the `app.php` file as the front controller

4. Install the dependencies:
```
$ cd my_project
$ composer install
```

5. Clear the cache:
```
$ php bin/console cache:clear
```

Your Symfony application is now ready to be deployed.

## Helpful links
- [Symfony CLI Tool](https://symfony.com/download)
- [Creating a Virtual Host](https://httpd.apache.org/docs/2.4/vhosts/examples.html)
- [Configuring the Web Server](https://symfony.com/doc/current/setup/web_server_configuration.html)
- [Installing Dependencies](https://getcomposer.org/doc/01-basic-usage.md)
- [Clearing the Cache](https://symfony.com/doc/current/setup/cache.html)

onelinerhub: [How to deploy a Symfony application?](https://onelinerhub.com/php-symfony/how-to-deploy-a-symfony-application)