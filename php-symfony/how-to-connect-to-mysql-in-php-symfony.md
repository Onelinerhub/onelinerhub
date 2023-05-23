# How to connect to MySQL in PHP Symfony?
// plain

To connect to MySQL in PHP Symfony, you need to configure the database connection parameters in the `config/packages/doctrine.yaml` file.

```yaml
# config/packages/doctrine.yaml
doctrine:
    dbal:
        url: '%env(resolve:DATABASE_URL)%'
        driver: 'pdo_mysql'
        server_version: '5.7'
        charset: utf8mb4
```

The example code above will connect to a MySQL database using the `DATABASE_URL` environment variable.

## Code explanation


- `doctrine`: The root key for Doctrine configuration.
- `dbal`: The Doctrine Database Abstraction Layer configuration.
- `url`: The URL of the database connection.
- `driver`: The database driver to use.
- `server_version`: The version of the database server.
- `charset`: The character set to use for the connection.

## Helpful links

- [Doctrine Configuration](https://symfony.com/doc/current/doctrine.html#configuration)
- [Database URL Format](https://symfony.com/doc/current/doctrine.html#configuring-the-database-url)

onelinerhub: [How to connect to MySQL in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-connect-to-mysql-in-php-symfony)