# How do I use the env() function in Laravel with PHP?
// plain

The `env()` function in Laravel is used to retrieve environment variables from the `.env` file. It is a wrapper around the PHP `getenv()` function, which retrieves variables from the system environment.

## Example


```
$database_name = env('DB_DATABASE');
echo $database_name;
```

## Output example
 `my_database`

The `env()` function takes two parameters, the first being the name of the environment variable, and the second being an optional default value to return if the environment variable does not exist.

1. `env('DB_DATABASE')` - retrieves the value of the `DB_DATABASE` environment variable from the `.env` file.
2. `env('DB_DATABASE', 'default_value')` - retrieves the value of the `DB_DATABASE` environment variable from the `.env` file, or returns `default_value` if the variable does not exist.

## Helpful links
- [Laravel Docs - Environment Configuration](https://laravel.com/docs/7.x/configuration#environment-configuration)
- [PHP Manual - getenv](https://www.php.net/manual/en/function.getenv.php)

onelinerhub: [How do I use the env() function in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-env---function-in-laravel-with-php)