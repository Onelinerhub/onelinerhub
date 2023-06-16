# How do I get an environment variable in Laravel using PHP?
// plain

You can get an environment variable in Laravel using PHP by using the `env()` helper function. This function takes two parameters, the first being the name of the environment variable, and the second being a default value to return if the environment variable does not exist.

For example:

```php
$database_name = env('DB_DATABASE', 'default_database');
```

The above code will first look for the `DB_DATABASE` environment variable. If it exists, the value of that environment variable will be assigned to `$database_name`. If it does not exist, then `default_database` will be assigned to `$database_name`.

**Parts of the Code**

1. `env()`: The helper function used to get the environment variable.
2. `DB_DATABASE`: The name of the environment variable being looked for.
3. `default_database`: The default value to be returned if the environment variable does not exist.

**Relevant Links**

- [Laravel Documentation - Environment Configuration](https://laravel.com/docs/7.x/configuration#environment-configuration)
- [Laravel Documentation - Helpers](https://laravel.com/docs/7.x/helpers#method-env)

onelinerhub: [How do I get an environment variable in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-get-an-environment-variable-in-laravel-using-php)