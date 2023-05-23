# Docker Compose and PHP Symfony usage
// plain

Docker Compose is a tool for defining and running multi-container Docker applications. It allows you to define a set of related services, networks and volumes in a single file, and then spin up the entire application with a single command.

PHP Symfony is a popular web application framework for PHP. It provides a set of reusable components, libraries and tools for building complex web applications.

Using Docker Compose and PHP Symfony together allows you to quickly and easily spin up a complete web application stack.

Example `docker-compose.yml` file:
```
version: '3'

services:
  web:
    image: php:7.2-apache
    volumes:
      - ./:/var/www/html
    ports:
      - 8080:80
```

This example will spin up a web server running PHP 7.2 and Apache, with the current directory mounted as the web root.

## Helpful links
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PHP Symfony Documentation](https://symfony.com/doc/current/index.html)

onelinerhub: [Docker Compose and PHP Symfony usage](https://onelinerhub.com/php-symfony/docker-compose-and-php-symfony-usage)