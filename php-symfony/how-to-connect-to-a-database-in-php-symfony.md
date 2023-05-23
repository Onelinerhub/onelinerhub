# How to connect to a database in PHP Symfony?
// plain

To connect to a database in PHP Symfony, you need to configure the database connection parameters in the `config/packages/doctrine.yaml` file.

```yaml
# config/packages/doctrine.yaml
doctrine:
    dbal:
        url: '%env(resolve:DATABASE_URL)%'
```

The `DATABASE_URL` environment variable should be set in the `.env` file.

```
# .env
DATABASE_URL=mysql://db_user:db_password@127.0.0.1:3306/db_name
```

## Code explanation


- `config/packages/doctrine.yaml`: This file is used to configure the database connection parameters.
- `.env`: This file is used to set the `DATABASE_URL` environment variable.
- `DATABASE_URL`: This environment variable contains the database connection parameters.

## Helpful links

- [Doctrine Configuration](https://symfony.com/doc/current/doctrine.html#configuration)
- [Environment Variables](https://symfony.com/doc/current/configuration/external_parameters.html#environment-variables)

onelinerhub: [How to connect to a database in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-connect-to-a-database-in-php-symfony)