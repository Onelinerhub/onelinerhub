# How to get an environment variable in PHP Symfony?
// plain

You can get an environment variable in PHP Symfony using the `getenv()` function.

## Example code

```
$envVar = getenv('ENV_VAR_NAME');
```

## Output example

```
$envVar = 'value of the environment variable';
```

The `getenv()` function takes a single argument, the name of the environment variable, and returns the value of the environment variable.

## Code explanation

- `getenv()`: function to get the value of an environment variable
- `ENV_VAR_NAME`: name of the environment variable

## Helpful links
- [PHP getenv() Function](https://www.w3schools.com/php/func_environment_getenv.asp)

onelinerhub: [How to get an environment variable in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-get-an-environment-variable-in-php-symfony)