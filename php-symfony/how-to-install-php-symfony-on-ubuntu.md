# How to install PHP Symfony on Ubuntu?
// plain

1. Install the Symfony installer using the following command:
```
$ sudo curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony
```
2. Make the installer executable:
```
$ sudo chmod a+x /usr/local/bin/symfony
```
3. Create a new Symfony project:
```
$ symfony new my_project_name
```
4. Install the necessary dependencies:
```
$ cd my_project_name
$ composer install
```
5. Start the built-in web server:
```
$ php bin/console server:run
```

## Helpful links
- [Symfony Installer](https://symfony.com/download)
- [Composer](https://getcomposer.org/)

onelinerhub: [How to install PHP Symfony on Ubuntu?](https://onelinerhub.com/php-symfony/how-to-install-php-symfony-on-ubuntu)