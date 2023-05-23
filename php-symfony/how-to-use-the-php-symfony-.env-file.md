# How to use the PHP Symfony .env file?
// plain

The `.env` file is a special file in Symfony that contains environment variables. It is used to store configuration values that are specific to the environment in which the application is running.

## Example code

```
APP_ENV=dev
APP_SECRET=abcdefghijklmnopqrstuvwxyz
```

The `APP_ENV` variable is used to set the environment in which the application is running. The `APP_SECRET` variable is used to store a secret key that is used to secure the application.

## Code explanation


- `APP_ENV`: This variable is used to set the environment in which the application is running. It can be set to `dev`, `prod`, or `test`.
- `APP_SECRET`: This variable is used to store a secret key that is used to secure the application. It should be a long, random string of characters.

## Helpful links

- [Symfony Documentation - Environment Variables](https://symfony.com/doc/current/configuration/external_parameters.html)

onelinerhub: [How to use the PHP Symfony .env file?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-.env-file)